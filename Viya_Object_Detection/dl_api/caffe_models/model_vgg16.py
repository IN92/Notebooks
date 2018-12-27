import sys

# VGG16 model definition
def VGG16_Model(s, inputCropType=None, inputChannelOffset=None):
   
   # quick error-checking and default setting
   if (inputCropType == None):
      inputCropType="NONE"
   else:
      if (inputCropType.upper() != "NONE") and (inputCropType.upper() != "UNIQUE"):
         sys.exit("ERROR: inputCropType can only be NONE or UNIQUE")
   
   if (inputChannelOffset == None):
      inputChannelOffset = [103.939, 116.779, 123.68]

   # instantiate model
   s.buildModel(model=dict(name='VGG16',replace=True),type='CNN')
 
   # input layer
   s.addLayer(model='VGG16', name='data',
              layer=dict( type='input', nchannels=3, width=224, height=224,
              randomcrop=inputCropType, offsets=inputChannelOffset))
 
   # conv1_1 layer: 64*3*3
   s.addLayer(model='VGG16', name='conv1_1',
              layer=dict( type='convolution', nFilters=64, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['data'])
 
   # conv1_2 layer: 64*3*3
   s.addLayer(model='VGG16', name='conv1_2',
              layer=dict( type='convolution', nFilters=64, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['conv1_1'])

   # pool1 layer: 2*2
   s.addLayer(model='VGG16', name='pool1',
              layer=dict(type='pooling',width=2, height=2, stride=2, pool='max'), 
              srcLayers=['conv1_2'])
 
   # conv2_1 layer: 128*3*3
   s.addLayer(model='VGG16', name='conv2_1',
              layer=dict( type='convolution', nFilters=128, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['pool1'])
 
   # conv2_2 layer: 128*3*3
   s.addLayer(model='VGG16', name='conv2_2',
              layer=dict( type='convolution', nFilters=128, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['conv2_1'])

   # pool2 layer: 2*2
   s.addLayer(model='VGG16', name='pool2',
              layer=dict(type='pooling',width=2, height=2, stride=2, pool='max'), 
              srcLayers=['conv2_2'])

   # conv3_1 layer: 256*3*3
   s.addLayer(model='VGG16', name='conv3_1',
              layer=dict( type='convolution', nFilters=256, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['pool2'])
 
   # conv3_2 layer: 256*3*3
   s.addLayer(model='VGG16', name='conv3_2',
              layer=dict( type='convolution', nFilters=256, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['conv3_1'])

   # conv3_3 layer: 256*3*3
   s.addLayer(model='VGG16', name='conv3_3',
              layer=dict( type='convolution', nFilters=256, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['conv3_2'])

   # pool3 layer: 2*2
   s.addLayer(model='VGG16', name='pool3',
              layer=dict(type='pooling',width=2, height=2, stride=2, pool='max'), 
              srcLayers=['conv3_3'])

   # conv4_1 layer: 512*3*3
   s.addLayer(model='VGG16', name='conv4_1',
              layer=dict( type='convolution', nFilters=512, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['pool3'])
 
   # conv4_2 layer: 512*3*3
   s.addLayer(model='VGG16', name='conv4_2',
              layer=dict( type='convolution', nFilters=512, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['conv4_1'])

   # conv4_3 layer: 512*3*3
   s.addLayer(model='VGG16', name='conv4_3',
              layer=dict( type='convolution', nFilters=512, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['conv4_2'])

   # pool4 layer: 2*2
   s.addLayer(model='VGG16', name='pool4',
              layer=dict(type='pooling',width=2, height=2, stride=2, pool='max'), 
              srcLayers=['conv4_3'])

   # conv5_1 layer: 512*3*3
   s.addLayer(model='VGG16', name='conv5_1',
              layer=dict( type='convolution', nFilters=512, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['pool4'])
 
   # conv5_2 layer: 512*3*3
   s.addLayer(model='VGG16', name='conv5_2',
              layer=dict( type='convolution', nFilters=512, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['conv5_1'])

   # conv5_3 layer: 512*3*3
   s.addLayer(model='VGG16', name='conv5_3',
              layer=dict( type='convolution', nFilters=512, width=3, height=3, 
                          stride=1, act='relu'), 
              srcLayers=['conv5_2'])

   # pool5 layer: 2*2
   s.addLayer(model='VGG16', name='pool5',
              layer=dict(type='pooling',width=2, height=2, stride=2, pool='max'), 
              srcLayers=['conv5_3'])
 
   # fc6 layer: 4096 neurons
   s.addLayer(model='VGG16', name='fc6',
              layer=dict(type='fullconnect',n=4096, act='relu', dropout=0.5), 
              srcLayers=['pool5'])

   # fc7 layer: 4096 neurons
   s.addLayer(model='VGG16', name='fc7',
              layer=dict(type='fullconnect',n=4096, act='relu', dropout=0.5), 
              srcLayers=['fc6'])

   # fc output layer: 1000 neurons
   s.addLayer(model='VGG16', name='fc8',
              layer=dict(type='output',n=1000, act='softmax'), 
              srcLayers=['fc7'])

#########################################################################################
if __name__ == "__main__":
   sys.exit("ERROR: this module defines the VGG-16 model.  Do not call directly.")