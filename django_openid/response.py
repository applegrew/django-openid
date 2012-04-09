from django.template.response import TemplateResponse as ActualTemplateResponse

class TemplateResponse(ActualTemplateResponse):
    '''
    Removed all old code so that django_openid can use django provided TemplateResponse.
    This sub-class exists since django_openid still referes to template_context from some places like auth.py.
    '''
    
    def __init__(self, request, template, context, *args, **kwargs):
        super(TemplateResponse, self).__init__(
            template, context, *args, **kwargs
        )
        self.template_context = context
    

# Even less verbose alias:
render = TemplateResponse
