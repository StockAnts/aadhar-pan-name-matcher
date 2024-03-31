
def clean_name(name):
    name = name.replace('.', ' ')
    name = name.split(' ')
    name = " ".join(filter(lambda x: x != "", name))
    return name
    

def is_exact(aadhar_name, pan_name):
    status = aadhar_name==pan_name
    print("Checking For Exact ---------------------------------------------------------------------------: ", status)
    return status

def same_aadhar_pan_reverse(aadhar_name, pan_name):
    status = aadhar_name==pan_name[::-1]
    print("Checking for same_aadhar_pan_reverse ----------------------------------------------------------: ", status)
    return status 


def aadhar_reverse_same_pan(aadhar_name, pan_name):
    status = aadhar_name[::-1]==pan_name
    print("Checking for aadhar_reverse_same_pan ----------------------------------------------------------: ", status)
    return status 


def reverse_name(name):
    return name[::-1]


def lists_to_dict(aadhar_name, pan_name):
    pairs = zip(aadhar_name, pan_name)
    result_dict = dict(pairs)
    return result_dict

def get_regular_format_name(name, skip_middle_name=False):
    splited_name = name.split(' ')
    
    if len(splited_name)>2: 
        last_name = splited_name[0]
        del splited_name[0]
        
        middle_name = splited_name[-1]
        del splited_name[-1]

        first_name = " ".join(splited_name)
    
        del splited_name

        if skip_middle_name:
            output = f'{first_name} {last_name}'
        else:  
            output = f'{first_name} {middle_name} {last_name}'
    else:
        first_name = splited_name[-1]
        last_name = splited_name[0]
        output = f'{first_name} {last_name}'
    return output 

def check_for_equality(splited_aadhar_name, splited_pan_name):

    st = []
    data_dict = lists_to_dict(splited_aadhar_name, splited_pan_name)
    print("data_dict", data_dict)
    for key, val in  data_dict.items():
        print("key", key, "value", val)
        if key == val:
            print("Same")
            st.append(True)
        elif val.startswith(key):
            print("Start with")
            st.append(True)
        elif key.startswith(val):
            print("val Start with key")
            st.append(True)
        else:
            print("In elase")
            st.append(False)
    status = all(st)
    print("Checking for equality --------------------------------------------------------------------------: ", status)
    return all(st)


def aadhar_last_name_rest_initial_with_pan(aadhar_name, pan_name, target="AADHAR"):
    formated_aadhar = aadhar_name
    formatted_pan = pan_name 

    if target == "AADHAR":formated_aadhar = get_regular_format_name(aadhar_name)
    if target == "PAN":formatted_pan = get_regular_format_name(pan_name)

    print("formated_aadhar   :", formated_aadhar)
    print("formatted_pan     :", formatted_pan)         

    splited_aadhar_name = formated_aadhar.split(' ')
    splited_pan_name = formatted_pan.split(' ')

    zipp = lists_to_dict(splited_aadhar_name, splited_pan_name)
    print("zipp", zipp)
    st = []
    
    for key, val in  zipp.items():
        print(key, val)
        if key == val:
            print("Same")
            st.append(True)
        elif val.startswith(key):
            print("val Start with key")
            st.append(True)
        elif key.startswith(val):
            print("key Start with val")
            st.append(True)
        else:
            print("In elase")
            st.append(False)

    status = all(st)
    print(":: Checking for aadhar_last_name_rest_initial_with_pan ----------------------------------------------------------: ", status)
    return all(st)

def match_aadhar(aadhar_name, pan_name):
    status = {}
    skipped = []
    try:
        aadhar_name = clean_name(aadhar_name).lower()
        pan_name = clean_name(pan_name).lower()
        
        print("aadhar_name clean    :", aadhar_name)
        print("pan_name clean       :", pan_name)

        if not aadhar_name or not pan_name: raise Exception("One of both details not available")
        
        is_matched = False

        splited_aadhar_name = aadhar_name.split(' ') 
        splited_pan_name = pan_name.split(' ')
        

        if is_exact(aadhar_name, pan_name):
            is_matched = True
            status['exact_name'] = status.get('exact_name', 0) + 1
        
        elif same_aadhar_pan_reverse(aadhar_name, pan_name):
            is_matched = True
            status['same_aadhar_pan_reverse'] = status.get('same_aadhar_pan_reverse', 0) + 1
        
        elif aadhar_reverse_same_pan(aadhar_name, pan_name):
            is_matched = True
            status['aadhar_reverse_same_pan'] = status.get('aadhar_reverse_same_pan', 0) + 1

        elif check_for_equality(splited_aadhar_name, splited_pan_name):
            is_matched = True
            status['check_for_equality'] = status.get('check_for_equality', 0) + 1

        elif aadhar_last_name_rest_initial_with_pan(aadhar_name, pan_name, target="AADHAR"):
            is_matched = True
            status['aadhar_last_name_rest_initial_with_pan'] = status.get('aadhar_last_name_rest_initial_with_pan', 0) + 1
        
        elif aadhar_last_name_rest_initial_with_pan(aadhar_name, pan_name, target="PAN"):
            is_matched = True
            status['pan_last_name_rest_initial_with_pan'] = status.get('pan_last_name_rest_initial_with_pan', 0) + 1

        elif len(splited_aadhar_name) < len(splited_pan_name):
            equal_len_pan = get_regular_format_name(pan_name, skip_middle_name=True)
            print("equal_len_pan", equal_len_pan)
            
            if is_exact(aadhar_name, pan_name):
                is_matched = True
                status['exact_name'] = status.get('exact_name', 0) + 1
            elif check_for_equality(splited_aadhar_name, equal_len_pan.split(' ')):
                is_matched = True
                status['check_for_equality'] = status.get('check_for_equality', 0) + 1
            
        return is_matched, ""
    except Exception as e:
        skipped.append({
            "aadhar name": aadhar_name,
            "pan_name": pan_name,
            "reason": str(e)
        })    
        return False, str(e)
    print("status", status)
    print("skipped", len(skipped))
    print("skipped", skipped)
    print("======================")


# aadhar_name = "Mayur Rajendra Fegde"
# # pan_name = "Fegde Mayur Rajendra"
# aadhar_name = "solanki rajesh hirabhai"
# pan_name = "rajesh hirabhai solanki"
# print(match_aadhar(aadhar_name=aadhar_name, pan_name=pan_name))