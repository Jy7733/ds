from heap import Heap
from Page import *


def lfu_sim(cache_slots):
  cache_hit = 0
  tot_cnt = 0
  misses = 0
  p = Page
  h = Heap
  l = LFUSimunl

  data_file = open("C:\\Users\\jaeyoung\\Desktop\\자료구조\\2023_과제\\lfu_sim\\lfu_sim\\linkbench.trc")


  for line in data_file.readlines():
    lpn = line.split()[0]    
    # Program here  
  for page_number in lpn :
    page = p.get_page(page_number)
    if page is None :
      misses += 1
      p.add_page(page_number)
    else:
      cache_hit += 1
    
    hit_ratio = cache_hit /  (cache_hit + misses) if cache_hit + misses > 0 else 0 
    
    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":
  for cache_slots in range(100, 1000, 100):
    lfu_sim(cache_slots)
