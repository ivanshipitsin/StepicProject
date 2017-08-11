def app(env,start_response):
    data = env['QUERY_STRING']
    output = data.split('&')
    body = ''
    for pair in output:
        body += pair + '\n'

    response_string = [('Content-type','text/plain')]
    start_response('200 OK',response_string)
    return [body.strip().encode()]
