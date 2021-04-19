import json,traceback

class Response():

    def __init__(self):
        pass

    def error_response_schema( self ):
        return {
                'HTTPStatusCode' : '',
                'description' : 'failed/succeeded',
                'error' : { 
                'description' : 'The error details',
                'name' : 'The human-readable, unique name of the error.',
                'message' : 'The message that describes the error.',
                'information_link' : 'The information link, or URI, that shows detailed information about this error for the developer.',                            
                'details' : [] } }

    def get_error_schema(self):
        return {
        'field' : 'request.json',
        'value' : 'The value of the field that caused the error.',
        'location' : 'The location of the field that caused the error. Value is `body`, `path`, or `query`.',
        'issue' : 'The unique, fine-grained application-level error code.',
        'description' : 'The human-readable description for an issue. The description can change over the lifetime of an API, so clients must not depend on this value.'
        }
    
    def get_success_response_schema(self):
        return {
        'HTTPStatusCode' : 'string_value',
        'description' : 'success',
        'message' : 'The message that describes the success action of the api.' }
        

    def error_response(self, val, loc, err, dsc, cde, err_typ, inf_lnk, msg):
        usr_err = self.get_error_schema()
        usr_err.update( { 'value' : val } )
        usr_err.update( { 'location' : loc } )
        usr_err.update( { 'issue' : err } )
        usr_err.update( { 'description' : dsc } )
        usr_err_res = self.error_response_schema()
        usr_err_res.update( { 'HTTPStatusCode' : cde } )
        usr_err_res.update( { 'description' : 'failed request' } )
        usr_err_res.get( 'error' ).update( { 'description':dsc } )
        usr_err_res.get( 'error' ).update( { 'name':err_typ } )
        usr_err_res.get( 'error' ).update( { 'information_link' : inf_lnk } )
        usr_err_res.get( 'error' ).update( { 'message' : msg } )
        usr_err_res.get( 'error' ).update( { 'details' : [usr_err] } )
        return usr_err_res

    def success_response( self, cde, msg ):
        scs_res=self.get_success_response_schema()
        scs_res.update( { 'HTTPStatusCode' : cde } )
        scs_res.update( { 'message' : msg } )
        return scs_res

    def par_success_response( self, cde, msg ):
        scs_res=self.get_success_response_schema()
        scs_res.update( { 'HTTPStatusCode' : cde } )
        scs_res.update( { 'message' : msg } )
        return scs_res

    def request_parser(self, items ):
        is_valid = 1
        try:
            item_count = len( items )
            for i in range(0, item_count ):
                if not ( items[i] and str( items[i] ).strip() ):
                    is_valid = 0
                is_valid *= is_valid
        except:
            traceback.print_exc()
            is_valid = 0
        return is_valid
    
    def exception_response( self, val ):
        try:
            err = 'exception occured in processing the :' + val
            dsc = 'exception occured in processing the :' + val + ' in the AWS LAMBDA service'
            return self.error_response( val, 'api request body', err, dsc, 500, 'server error', '', dsc )

        except:
            traceback.print_exc()
            err = 'exception occured in processing the :' + val
            dsc = 'exception occured in processing the :' + val + ' in the AWS LAMBDA service'
            return self.error_response( val, 'api request body', err, dsc, 500, 'server error', '', dsc )
    
    def clnt_exception_response( self, val, error_msg ):
        try:
            err = error_msg
            dsc = 'exception occured in processing the :' + val + ' in the AWS LAMBDA service'
            return self.error_response( val, 'api request body', err, dsc, 500, 'server error', '', dsc )

        except:
            traceback.print_exc()
            return self.exception_response( val )

    def null_err_response( self, val ):
        try:
            dsc = val + ' in the request body should not be null object'
            err = val + ' in the request body is null object'
            return self.error_response( val, 'api request body', err, dsc, 400, 'validation error', '', dsc )

        except:
            traceback.print_exc()
            return self.exception_response( val )

    def resou_crea_failed_res( self, val ):
        try:
            dsc = val + ' resource creation failed'
            err = val + ' resource could not be successfully created'
            return self.error_response( val, 'api request body' , err,dsc, 500, 'server error', '', dsc )

        except:
            traceback.print_exc()
            return self.exception_response( val )

    
