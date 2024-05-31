from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    return HttpResponse('this is homepage')
def about(request):
    return render(request,'aboutme.html')
    return HttpResponse('''
Hello everyone my name is Dipankar Saha, and I am a geography teacher in
Coochbehar College.My age is 27 years.I am doing phd under the proper guidance of
my respected teacher Mr.Tapan Kumar Das.In my home I used to live with my mother,
father and my big brother Basu.He is a very nice brother.However as my hobby I love
to ride bike a lot.In my off days I used to go to nearby tours with my friends,
However I also love to eat.My favourite dish is mutton biriyani made by my mom.''')
def services(request):
    return render(request,'myworks.html')
    return HttpResponse('''1.LAND CAPABILITY ASSESSMENT OF ALIPURDUAR DISTRICT______FOR AGRICULTURAL SUITABILITY USING MULTI-CRITERIA BASED DECISION-MAKING APPROACH:
Soil degradation is an urgent concern for its crucial role in sustaining life on Earth. The gradual process of soil formation is threatened by the growing demands of a burgeoning human population. Agriculture, the primary driver of this demand, often leads to soil deterioration due to unsustainable practices and poor land management. Failure to consider soil quality and suitability for crops can severely impact agricultural productivity. The present study has assessed the land capability classification of Alipurduar District through Multi-Criteria Based Decision-Making Approach using AHP Method, utilizing 11 parameters. The findings reveals diverse Land Capability Classifications (LCC) in the region. Approximately 21% and 29% of the district's land are classified under Class II (Moderately Good Cultivable Land) and Class III (Fairly Good Cultivable Land) respectively, providing favorable conditions for farming activities. Conversely, 36% and 14% are designated as Class IV (Well Suited for Grazing) and Class V (Fairly Well Suited for Grazing & Forestry or Grazing), indicating lesser suitability for agriculture. Validation of the Land Capability Classification was conducted using receiver operating characteristic area under the curve (ROC-AUC) analysis, yielding a value of 0.871, with significance value of 0.00 and a standard error of 0.052. These results and subsequent analyses highlight the importance of sustainable land management practices to preserve soil health and ensure agricultural productivity in the region.
_______________________________________________________________________________________2.ASSESSMENT OF POTENTIAL LAND SUITABILITY FOR ECONOMIC ACTIVITY USING AHP AND GIS TECHNIQUES IN DROUGHT PRONE GANDHESWARI WATERSHED, BANKURA DISTRICT IN WEST BENGAL:

Abstract
Land is essential component of nature for performing any type of economic activity but availability of land is limited and more or less fixed. Enormous population pressure on land is a contemporary phenomenon. So assessment of land suitability for different economic activity is a very imperative for natural resource management. The present study aims to determine suitability of land for agriculture, pasture, forestry and industry. GIS based Analytical Hierarchy Process (AHP) technique is used for land suitability classification. Versatile thematic components, namely soil-depth, soil-texture, river-buffer, MNDWI (Modified Normalized Differentiate Water Index), NDVI (Normalized Differential Vegetation Index), Groundwater, rainfall, landuse and landcover, curvature, slope and elevation are integrated in a GIS environment. It was produced based on weighted overly by using AHP technique. Land suitability of drought prone Gandheswari Watershed is divided into seven land suitability Classes, namely, Class-I: Highly suitable for agriculture [84 km2], Class-II: Moderately suitable for agriculture [81 km2], Class-III: Low to Moderately suitable for agriculture [76 km2], Class-IV: Transitional zone-I, having less agriculture, agro-forestry and pasture [57 km2], Class-V: Suitable for Agro-forestry and pastureland [51 km2], Class-VI: Transitional zone-ii [26 km2], Class-VII: Suitable for industrialization (25 km2). The land suitability map of the study area has been validated by using present landuse and landcover ground truth point. Then, the Receiver Operating Characteristic (ROC) curve is prepared for validation of the methodology used in this work. The result of Area Under the Curve (AUC) is good indicating an accuracy of (0.72) 72%. The result of this Potential land suitability for economic activity can be helpful in sustainable land use and land cover development, land conservation planning and strategy formulation for management of land.''')

    
def photos(request):
    return render(request,'myphotos.html')
    return HttpResponse('THIS IS MY PHOTOS AND VIDEOS PAGE')
