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
SEARCH_URL = 'http://www.amazon.de/b/ref=amb_link_188447267_1/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981666031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Schwimmen-Baden-Bademode-Damen/b/ref=amb_link_188447267_2/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981860031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Blusen-Damen-Tunika-Tuniken/b/ref=amb_link_188447267_3/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981720031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Hosen-Damen/b/ref=amb_link_188447267_4/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981874031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/b/ref=amb_link_188447267_5/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981832031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Jeans-Damen/b/ref=amb_link_188447267_6/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981723031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Jumpsuits-Damen/b/ref=amb_link_188447267_7/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981724031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/s/ref=amb_link_188447267_8/280-4163933-9570166?ie=UTF8&bbn=1981665031&lo=clothing&rh=i%3Aclothing%2Cn%3A77028031%2Cn%3A!78689031%2Cn%3A1981665031%2Cn%3A1981722031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Kleider-Kleid-Abendkleider/b/ref=amb_link_188447267_9/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981721031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/s/ref=amb_link_188447267_10/280-4163933-9570166?ie=UTF8&bbn=1981665031&lo=clothing&rh=i%3Aclothing%2Cn%3A77028031%2Cn%3A!78689031%2Cn%3A1981665031%2Cn%3A1981853031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Leggings-Damen/b/ref=amb_link_188447267_11/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981732031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/b/ref=amb_link_188447267_12/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981825031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Overalls-Damen/b/ref=amb_link_188447267_13/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981836031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/b/ref=amb_link_188447267_14/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981725031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/R%C3%B6cke-Rock/b/ref=amb_link_188447267_15/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981838031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/s/ref=amb_link_188447267_16/280-4163933-9570166?ie=UTF8&bbn=1981665031&lo=clothing&rh=i%3Aclothing%2Cn%3A77028031%2Cn%3A!78689031%2Cn%3A1981665031%2Cn%3A1981839031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Shorts-Hotpants-Damen/b/ref=amb_link_188447267_17/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981837031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/b/ref=amb_link_188447267_18/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981844031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/s/ref=amb_link_188447267_19/280-4163933-9570166?ie=UTF8&bbn=1981665031&lo=clothing&rh=i%3Aclothing%2Cn%3A77028031%2Cn%3A!78689031%2Cn%3A1981665031%2Cn%3A1981704031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/b/ref=amb_link_188447267_20/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981859031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/b/ref=amb_link_188447267_21/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981869031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Umstandsmode-Schwangerschaftsmode/b/ref=amb_link_188447267_22/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981774031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Unterw%C3%A4sche-Damen/b/ref=amb_link_188447267_23/280-4163933-9570166?ie=UTF8&lo=clothing&node=1981733031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=708833887&pf_rd_i=1981665031',
'http://www.amazon.de/Mode-Basics/b/ref=amb_link_195850707_1/280-4163933-9570166?ie=UTF8&node=366048031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=784382567&pf_rd_i=1981665031',
'http://www.amazon.de/Mode-Premium-Marken/b/ref=amb_link_195850707_2/280-4163933-9570166?ie=UTF8&node=904576031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=784382567&pf_rd_i=1981665031',
'http://www.amazon.de/trachten-dirndl-lederhosen/b/ref=amb_link_195850707_3/280-4163933-9570166?ie=UTF8&node=1981533031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=784382567&pf_rd_i=1981665031',
'http://www.amazon.de/Sale-Bekleidung/b/ref=amb_link_195850707_4/280-4163933-9570166?ie=UTF8&node=246336031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=784382567&pf_rd_i=1981665031',
'http://www.amazon.de/b/ref=amb_link_195850707_5/280-4163933-9570166?ie=UTF8&node=5430589031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=784382567&pf_rd_i=1981665031',
'http://www.amazon.de/b/ref=amb_link_195850707_6/280-4163933-9570166?ie=UTF8&node=8641302031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0SD7CAC70RY0T8T98TJ0&pf_rd_t=101&pf_rd_p=784382567&pf_rd_i=1981665031',
'http://www.amazon.de/b/ref=amb_link_188448547_1?ie=UTF8&lo=clothing&node=1981299031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/b/ref=amb_link_188448547_2?ie=UTF8&lo=clothing&node=1981381031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/Schwimmen-Baden-Bademode-Herren/b/ref=amb_link_188448547_3?ie=UTF8&lo=clothing&node=1981391031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/Hemden/b/ref=amb_link_188448547_4?ie=UTF8&lo=clothing&node=1981367031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/b/ref=amb_link_188448547_5?ie=UTF8&lo=clothing&node=1981399031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/b/ref=amb_link_188448547_6?ie=UTF8&lo=clothing&node=1981362031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/Jeans-Herren/b/ref=amb_link_188448547_7?ie=UTF8&lo=clothing&node=1981350031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/Kapuzenpullover-Herren/b/ref=amb_link_188448547_8?ie=UTF8&lo=clothing&node=1981349031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/b/ref=amb_link_188448547_9?ie=UTF8&lo=clothing&node=1981356031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/s/ref=amb_link_188448547_10?ie=UTF8&bbn=1981298031&lo=clothing&rh=i%3Aclothing%2Cn%3A77028031%2Cn%3A!78689031%2Cn%3A1981298031%2Cn%3A1981366031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/b/ref=amb_link_188448547_11?ie=UTF8&lo=clothing&node=1981351031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/s/ref=amb_link_188448547_12?ie=UTF8&bbn=1981298031&lo=clothing&rh=i%3Aclothing%2Cn%3A77028031%2Cn%3A!78689031%2Cn%3A1981298031%2Cn%3A1981372031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/b/ref=amb_link_188448547_13?ie=UTF8&lo=clothing&node=1981371031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/b/ref=amb_link_188448547_14?ie=UTF8&lo=clothing&node=1981377031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/s/ref=amb_link_188448547_15?ie=UTF8&bbn=1981298031&lo=clothing&rh=i%3Aclothing%2Cn%3A77028031%2Cn%3A!78689031%2Cn%3A1981298031%2Cn%3A1981336031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/Sweatshirts-Herren/b/ref=amb_link_188448547_16?ie=UTF8&lo=clothing&node=1981390031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/b/ref=amb_link_188448547_17?ie=UTF8&lo=clothing&node=1981394031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/Unterw%C3%A4sche-Herren/b/ref=amb_link_188448547_18?ie=UTF8&lo=clothing&node=1981400031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=708835807&pf_rd_i=1981298031',
'http://www.amazon.de/Mode-Basics/b/ref=amb_link_189999047_1?ie=UTF8&node=366048031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=784382387&pf_rd_i=1981298031',
'http://www.amazon.de/Mode-Premium-Marken/b/ref=amb_link_189999047_2?ie=UTF8&node=904576031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=784382387&pf_rd_i=1981298031',
'http://www.amazon.de/trachten-dirndl-lederhosen/b/ref=amb_link_189999047_3?ie=UTF8&node=1981533031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=784382387&pf_rd_i=1981298031',
'http://www.amazon.de/Sale-Bekleidung/b/ref=amb_link_189999047_4?ie=UTF8&node=246336031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=784382387&pf_rd_i=1981298031',
'http://www.amazon.de/b/ref=amb_link_189999047_5?ie=UTF8&node=5430588031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=784382387&pf_rd_i=1981298031',
'http://www.amazon.de/b/ref=amb_link_189999047_6?ie=UTF8&node=8641302031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-4&pf_rd_r=0XS0NMK921QKY7F9BRDZ&pf_rd_t=101&pf_rd_p=784382387&pf_rd_i=1981298031',
'http://www.amazon.de/Kinderbekleidung-Kinderkleidung-Kindermode/b/ref=sd_allcat_sa_app_de_kids?ie=UTF8&node=2614055031',
'http://www.amazon.de/Babymode-Babykleidung-Baby/b/ref=sd_allcat_sa_app_de_baby?ie=UTF8&node=1981001031',
'http://www.amazon.de/Ballerinas-Damen/b/ref=sh_browsesh_damen_ballerinas?ie=UTF8&lo=shoes&node=1760305031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsesh_damen_boot?ie=UTF8&lo=shoes&node=1760306031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsesh_damen_clogs?ie=UTF8&lo=shoes&node=1760307031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/Espadrilles/b/ref=sh_browsesh_damen_espadrilles?ie=UTF8&lo=shoes&node=1760308031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsesh_damen_hausschuhe?ie=UTF8&lo=shoes&node=1760309031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsesh_damen_mary?ie=UTF8&lo=shoes&node=1760310031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/High-Heels-Pumps/b/ref=sh_browsesh_damen_pumps?ie=UTF8&lo=shoes&node=1760311031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/Sandalen-Sandaletten-Damen/b/ref=sh_browsesh_damen_sandalen?ie=UTF8&lo=shoes&node=1760312031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsesh_damen_schnuer?ie=UTF8&lo=shoes&node=1760313031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/Sicherheitsschuhe-Arbeitsschuhe/b/ref=sh_browsesh_damen_sicher?ie=UTF8&lo=shoes&node=1760314031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsesh_damen_slipper?ie=UTF8&lo=shoes&node=1760315031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsesh_damen_sneaker?ie=UTF8&lo=shoes&node=1760316031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsesh_damen_sport?ie=UTF8&lo=shoes&node=1760317031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/Stiefeletten-Damen/b/ref=sh_browsesh_damen_stiefel?ie=UTF8&lo=shoes&node=1760365031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsesh_damen_zehen?ie=UTF8&lo=shoes&node=1760366031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=718490327&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsewmn_hw15?ie=UTF8&node=7003984031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=811608847&pf_rd_i=1760304031',
'http://www.amazon.de/Designer-Shop-Schuhe-Handtaschen/b/ref=sh_browsewmn_designer?ie=UTF8&node=2690577031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=811608847&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsewmn_mii?ie=UTF8&node=8641302031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=1PW13320984QMFJ06Q4R&pf_rd_t=101&pf_rd_p=811608847&pf_rd_i=1760304031',
'http://www.amazon.de/b/ref=sh_browsesh_herren_boot?ie=UTF8&lo=shoes&node=1760368031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/b/ref=sh_browsesh_herren_clog?ie=UTF8&lo=shoes&node=1760369031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/b/ref=sh_browsesh_herren_espandrille?ie=UTF8&lo=shoes&node=1760370031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/Hausschuhe-Pantoletten-H%C3%BCttenschuhe/b/ref=sh_browsesh_herren_hausschuhe?ie=UTF8&lo=shoes&node=1760371031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/b/ref=sh_browsesh_herren_sandals?ie=UTF8&lo=shoes&node=1760372031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/b/ref=sh_browsesh_herren_schnuerer?ie=UTF8&lo=shoes&node=1760373031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/b/ref=sh_browsesh_herren_sicher?ie=UTF8&lo=shoes&node=1760374031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/b/ref=sh_browsesh_herren_slipper?ie=UTF8&lo=shoes&node=1760375031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/Herren-Sneaker/b/ref=sh_browsesh_herren_sneaker?ie=UTF8&lo=shoes&node=1760376031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/b/ref=sh_browsesh_herren_sport?ie=UTF8&lo=shoes&node=1760377031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/b/ref=sh_browsesh_herren_stiefel?ie=UTF8&lo=shoes&node=1760425031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/Zehentrenner-Herren/b/ref=sh_browsesh_herren_zehen?ie=UTF8&lo=shoes&node=1760426031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-2&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=666529007&pf_rd_i=1760367031',
'http://www.amazon.de/b/ref=sh_browsemen_hw15?ie=UTF8&node=7004427031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=811608807&pf_rd_i=1760367031',
'http://www.amazon.de/Designer-Shop-Schuhe-Handtaschen/b/ref=sh_browsemen_designer?ie=UTF8&node=2690577031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=811608807&pf_rd_i=1760367031',
'http://www.amazon.de/b/ref=sh_browsemen_mii?ie=UTF8&node=8641302031&pf_rd_m=A3JWKAKR8XB7XF&pf_rd_s=merchandised-search-left-3&pf_rd_r=1JDD821M0B886AD5MGS1&pf_rd_t=101&pf_rd_p=811608807&pf_rd_i=1760367031',
'http://www.amazon.de/Kinderschuhe/b/ref=sd_allcat_sa_sho_de_kids?ie=UTF8&node=2145731031',
('http://www.amazon.de/Babyschuhe/b/ref=sd_allcat_sa_sho_de_baby?ie=UTF8&node=1760297031',
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
