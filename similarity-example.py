from scipy import spatial
import random 

## Set a random seed for reproducibility
random.seed(1337)

## Generate some random vectors
embedding_01 = [random.uniform(-1, 1) for i in range(10)]
embedding_02 = [random.uniform(-1, 1) for i in range(10)]

## Cosine similarity.  
## 1 - spatial.distance.cosine because higher = more similar
def cos_similarity(a, b):
    return 1 - spatial.distance.cosine(a, b)

cos_similarity(embedding_01, embedding_02)

## Euclidian distance
## You'll definitely want to figure out a way of normalizing this.  One way is probably dist/max_dist 
spatial.distance.euclidean(embedding_01, embedding_02)  

## See https://docs.scipy.org/doc/scipy/reference/spatial.distance.html#module-scipy.spatial.distance for other distance measures you might be able to leverage.

