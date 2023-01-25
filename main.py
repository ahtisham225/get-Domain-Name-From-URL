# Run the File with python main.py
# CHANGE THE VARIABLE URL WITH THE URL YOU WANT DOMAIN FOR.

def main(input_string):
    # Taking input from User. a Url String
    # Domain name to Store The Returned Value
    print(input_string)
    Domain_name = ""
    # Split the input string by backslash
    x = input_string.split("/")
    # if input URL string contain HTTPs or HTTP
    if (x[0] == "https:" or x[0] == "http:"):
        x = x[2].split(".")
        # //if Input URL String only contain www. without any Http or https.
    else:
        x = x[0].split(".")
    # if input URL without www. or subdomain
    if (len(x) == 2):
        Domain_name = x[0]
        # if input URL is with www. or subdomain
    else:
        Domain_name = x[1]
    print("The Domain Name is ", Domain_name)


URL = "www.hecodesit.com"
main(URL)
