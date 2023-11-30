from gestor.models import UserFeedback

def getFeedbacksUser(user):
    feedback = UserFeedback.objects.filter(user=user)

    return feedback