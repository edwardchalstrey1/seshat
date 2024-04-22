from .models import SeshatPrivateCommentPart
from ..accounts.models import Seshat_Expert

def notifications(request):
    # Fetch the data you need
    #print("Halooooooooooooooooo")
    if request.user.is_authenticated:
        try:
            my_expert =  Seshat_Expert.objects.get(user_id=request.user.id)
            all_my_private_comments = SeshatPrivateCommentPart.objects.filter(private_comment_reader__id=my_expert.id)
            notifications_count = len(all_my_private_comments)
        except:
            notifications_count = 0
    else:
        notifications_count = 0

    # Return the data as a dictionary
    return {'notifications_count': notifications_count}