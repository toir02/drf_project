from rest_framework import serializers

from education.models import Course, Lesson, Payment, Subscription
from education.services import create_payment_intent, retrieve_payment_intent
from education.validators import LinkValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkValidator(field='link')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField(read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    subscription = serializers.SerializerMethodField(read_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get('context').get('request')

    @staticmethod
    def get_lessons_count(instance):
        return instance.lessons.count()

    def get_subscription(self, instance):
        subscription = Subscription.objects.filter(user=self.request.user, course=instance).first()

        if subscription and subscription.is_active:
            return True
        else:
            return False

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    payment_stripe = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Payment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = kwargs.get('context').get('request')

    def get_payment_stripe(self, instance):
        if self.request.method == 'POST':
            payment_stripe_id = create_payment_intent(instance.amount)
            obj_payment = Payment.objects.get(id=instance.id)
            obj_payment.payment_stripe_id = payment_stripe_id
            obj_payment.save()

            return retrieve_payment_intent(payment_stripe_id)

        if self.request.method == 'GET':
            if not instance.payment_stripe_id:
                return None
            return retrieve_payment_intent(instance.payment_stripe_id)


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
