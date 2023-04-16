class SetRemoteAddrMiddleware(object):
    def process_request(self, request):
        if not request.META.get('REMOTE_ADDR', None):
            try:
                request.META['REMOTE_ADDR'] = request.META['HTTP_X_REAL_IP']
            except KeyError:
                request.META['REMOTE_ADDR'] = '158.160.32.231'
