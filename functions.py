


def bsearch(id,all,k,l):
	if(k<l):
		mid = k + (l-k)/2
		# print k,l,mid
		# print id,all[mid]
		if(id.strip() == all[mid]):
			return 1;
		elif(id < all[mid]):
			l = mid
			return bsearch(id,all,k,l)
		elif(id>all[mid]):
			k=mid+1
			return bsearch(id,all,k,l)
	else:
		return 0;
