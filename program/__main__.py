import io, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)

googleCredsEnvVarName = 'GOOGLE_APPLICATION_CREDENTIALS'
if os.getenv(googleCredsEnvVarName) is None:
	print(f'Please set your "{googleCredsEnvVarName}" environment variable and try again')
	sys.exit(1)

from google.cloud import vision
import image_string_swap as imgstrswap

client = vision.ImageAnnotatorClient()

# file_path = input('Please provide the absolute image path: ')
# with io.open(file_path, 'rb') as image_file:
# 	content = image_file.read()
# image = vision.types.Image(content=content)

image = vision.types.Image()
image.source.image_uri = input('Please provide the image uri: ')

response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')

for text in texts:
	print('\n"{}"'.format(text.description))

	vertices = (['({},{})'.format(vertex.x, vertex.y)
				for vertex in text.bounding_poly.vertices])

	print('bounds: {}'.format(','.join(vertices)))