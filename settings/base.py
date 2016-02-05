# -*- coding: utf-8 -*-


class QuoteParam:
    ALL = 1
    MINIMAL = 0
    NONE = 3
    NONNUMERIC = 2

# Урл для поиска товаров. Вместо '{}' будут подставлены поисковые выражения.
# Если поисковые выражения использоваться не будут, то нужно заклучить урл в
# круглые скобки и можно будет через запятую перечислить список урлов. Важно!
# При использовании списка не указывайте {}
#
# Примеры:
#
# Списком без поисковых фраз
# SEARCH_URL = ("http://www.amazon.de/s/ref=nb_sb_noss?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=node%3D1981733031&field-keywords=", )
#
# С поисковыми фразами
# SEARCH_URL = "http://www.amazon.de/s/ref=nb_sb_noss?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=node%3D1981733031&field-keywords={}"
SEARCH_URL = ('http://www.amazon.de/Babyschuhe/b/ref=sd_allcat_sa_sho_de_baby?ie=UTF8&node=1760297031',
'http://www.amazon.de/Schmuck-Charms-Ohrringe-Ketten/b/ref=sd_allcat_sa_de_jewelry?ie=UTF8&node=327472011',
'http://www.amazon.de/Damenuhren/b/ref=DE_W_Main_LeftNav_Women?ie=UTF8&node=198911031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/Herrenuhren/b/ref=DE_W_Main_LeftNav_Men?ie=UTF8&node=198912031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/Kinderuhren/b/ref=DE_W_Main_LeftNav_Kids?ie=UTF8&node=198913031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_Wristwatches?ie=UTF8&node=198795031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/Hochwertige-Luxusuhren/b/ref=DE_W_Main_LeftNav_Luxury?ie=UTF8&node=198796031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_Pocketwatches?ie=UTF8&node=198797031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_Tools?ie=UTF8&node=198799031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_watchWinder?ie=UTF8&node=198802031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_Boxes?ie=UTF8&node=198801031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_Watchbands?ie=UTF8&node=198800031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/gp/search/other/ref=DE_W_Main_LeftNav_Brands?ie=UTF8&bbn=198795031&pickerToList=brandtextbin&qid=1321966539&rd=1&rh=n%3A193707031%2Cn%3A!193708031%2Cn%3A198795031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_Analog?ie=UTF8&rh=n%3A198795031%2Cp_n_feature_seven_browse-bin%3A198811031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_Digital?ie=UTF8&rh=n%3A198795031%2Cp_n_feature_seven_browse-bin%3A198812031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_Chrono?ie=UTF8&rh=n%3A198795031%2Cp_n_feature_seven_browse-bin%3A212841031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_Automatic?ie=UTF8&rh=n%3A198795031%2Cp_n_feature_browse-bin%3A198826031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_10?ie=UTF8&bbn=193707031&page=1&rh=n%3A193707031%2Cp_36%3A1000-2000&sort=salesrank&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_20?ie=UTF8&rh=n%3A193707031%2Cp_36%3A197639031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_50?ie=UTF8&rh=n%3A193707031%2Cp_36%3A197640031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_100?ie=UTF8&rh=n%3A193707031%2Cp_36%3A197641031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_plus200?ie=UTF8&rh=n%3A193707031%2Cp_36%3A197642031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/s/ref=DE_W_Main_LeftNav_Prime?ie=UTF8&bbn=193707031&rh=i%3Awatches%2Cn%3A193707031%2Cp_76%3A197653031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/Sonderangebote-Restposten-Uhren/b/ref=DE_W_Main_LeftNav_Deals?ie=UTF8&node=198908031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/Uhren/b/ref=DE_W_Main_LeftNav_WarehouseDeals?ie=UTF8&me=A8KICS1PHF7ZO&node=310438031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=675742627&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_1?ie=UTF8&node=1366247031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_2?ie=UTF8&node=3954414031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_3?ie=UTF8&node=1837497031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_4?ie=UTF8&node=2179958031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/Casio-Shop-Uhren-Schmuck/b/ref=amb_link_158992907_5?ie=UTF8&node=344500011&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_6?ie=UTF8&node=514307031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_7?ie=UTF8&node=3600367031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_8?ie=UTF8&node=1950445031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_9?ie=UTF8&node=683221031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_10?ie=UTF8&node=3867574031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_11?ie=UTF8&node=8561163031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_12?ie=UTF8&node=2361237031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_13?ie=UTF8&node=522386031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_14?ie=UTF8&node=5403386031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_15?ie=UTF8&lo=watches&node=4913461031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_16?ie=UTF8&node=1366253031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_17?ie=UTF8&node=1622272031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_18?ie=UTF8&node=1976570031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_19?ie=UTF8&node=3426602031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_20?ie=UTF8&node=533566031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_21?ie=UTF8&node=364893031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_22?ie=UTF8&node=1723407031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_23?ie=UTF8&node=1622654031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_24?ie=UTF8&node=1795360031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/Polar-Onlineshop-Elektronik/b/ref=amb_link_158992907_25?ie=UTF8&node=213000031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_26?ie=UTF8&node=1976571031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_27?ie=UTF8&node=1366252031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_28?ie=UTF8&node=1801677031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_29?ie=UTF8&node=2090382031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/Suunto-Shop/b/ref=amb_link_158992907_30?ie=UTF8&node=425826031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_31?ie=UTF8&node=1944992031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_32?ie=UTF8&node=1400230031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_33?ie=UTF8&node=4487729031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_34?ie=UTF8&node=3867563031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/b/ref=amb_link_158992907_35?ie=UTF8&node=824396031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=03J8R2W6W384JPXKVJ42&pf_rd_t=101&pf_rd_p=758768807&pf_rd_i=193707031',
'http://www.amazon.de/Handtaschen-Taschen/b/ref=sd_allcat_sa_de_hbags?ie=UTF8&node=1760236031',
'http://www.amazon.de/koffer-rucks%C3%A4cke-taschen/b/ref=sd_allcat_sa_de_luggage?ie=UTF8&node=2454118031',
'http://www.amazon.de/gp/feature.html/ref=sd_allcat_sa_de_buyvip?ie=UTF8&docId=1000728993')
# Поисковые выражения
PHRASES = (
    'Bra damen',
)

# настройка параметров записи в csv файл
OUT_FILE = 'out.csv',  # имя файла для вывода
CSV = dict(
    delimiter=':',  # разделитель значений
    quoting=QuoteParam.MINIMAL,  # параметр цитирования
    quotechar='`',  # символ цитирования
    lineterminator='|'  # разделитель строк
)

#
USE_PROXY = False
