import pnutpy
pnutpy.api.add_authorization_token(<Access Token Here>)

# Create a post
post, meta = pnutpy.api.create_post(data={'text':'Hello pnut.io from pnutpy!'})
