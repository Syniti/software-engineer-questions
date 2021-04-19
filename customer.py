import traceback, string
class Customer:
    def __init__( self ):
        self.in_valid_customers = set()
        self.duplicate_customers = set()
        self.customer_duplicate_checker = {}

    def check_validity( self, customer ):
        #check if the current customer daat is valid or invalid.
        isValid = 0
        try:
            #inValid customer data
            if not ( customer.get( "name") and customer.get( "address") and customer.get( "zip") ):
                return isValid
            else:
                #Valid customer data.
                isValid = 1
                return isValid
        except:
            traceback.print_exc()
            return isValid

    def add_invalid_list( self, inValid_customer ):
        #add the current inValid customer to the Invalid custoemr collection.
        try:
            self.in_valid_customers.add( inValid_customer.get( "id" ) )
        except:
            traceback.print_exc()
        
    def build_unique_id( self, customer ):
        #build the unique id for each customer.
        #unique_id = name+address+zip
        uni_cus_id = ""
        try:
            check_list = [ customer.get( "name" ), customer.get( "address" ), customer.get( "zip" ) ]
            for check_item in check_list:
                if check_item:
                    uni_cus_id = "{}{}".format( uni_cus_id, check_item.strip().replace(" ", "") )
                else:
                    uni_cus_id = "{}{}".format( uni_cus_id, "_" )
            return uni_cus_id
        except:
            traceback.print_exc()
            uni_cus_id = ""
            return uni_cus_id

    def validate_duplicate_customer( self, customer , unique_customer_id ):
        #validate if the generated customer id is unique or duplicate.
        try:
            # unique id.
            if unique_customer_id not in self.customer_duplicate_checker:
                self.customer_duplicate_checker.update( { unique_customer_id : customer.get( "id" )  } )
            else:
                # duplicate id.
                self.duplicate_customers.add( self.customer_duplicate_checker.get( unique_customer_id ) )
                self.duplicate_customers.add( customer.get( "id" ) )
                self.customer_duplicate_checker.update( { unique_customer_id : customer.get( "id" ) } )
        except:
            traceback.print_exc()

    def merge_inVaid_duplicate_customer_set( self ):
        try:
            return self.in_valid_customers | self.duplicate_customers    
        except:
            traceback.print_exc()