import json, traceback
from response import Response
from customer import Customer

def lambda_handler(event, context):
    #interface handler.
    try:
        #response_object.
        response_obj = Response()
        
        #Extract and validate the collection containing the customer data.
        customer_data = event.get( "data" )
        is_valid = response_obj.request_parser( customer_data )
        
        #Exit_point: failure, no data to process.
        if not is_valid:
            return response_obj.error_response( "data","path","data empty","no customer data to pocss",404,"client error","","in_valid customer data")
            
        #customer object.
        cust_obj = Customer()

        #Iterate over all the customer data.
        for curr_customer in customer_data:
            #check_validity.
            isCustomerValid = cust_obj.check_validity( curr_customer )
            
            #build Invalid customer list.
            if not isCustomerValid:
                # add the inValid customer to the inValidCustomerList.
                cust_obj.add_invalid_list( curr_customer )

            #build unique_id.
            unique_cus_id = cust_obj.build_unique_id( curr_customer )
            
            #build the duplicate list.
            cust_obj.validate_duplicate_customer( curr_customer, unique_cus_id )

        #build the in_valid set.
        inValid_customers = cust_obj.merge_inVaid_duplicate_customer_set()

        #print the invalid customers.
        for customer in inValid_customers:
            print(customer) 

        return response_obj.success_response( 200, "invalid_customers_marked" )

    except:
        traceback.print_exc()
        return response_obj.exception_response( "invalid_data in the request payload" )