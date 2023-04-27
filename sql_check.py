def check(text1, text2, text4):
    sqlKeyWords = "select ,union ,asc ,desc ,in ,like ,into ,exec ,from "
    sqlKeyWords += ",update ,insert ,delete ,count ,asc( ,char( ,chr( ,drop ,table ,truncat "
    sqlKeyWords += ",mid( ,abs( ,= ,-- ,<script ,/script "
    sqlKeyWords += ",where ,join ,create ,alter ,cast ,exists , or , and ,order by ,group by "
    sqlkey = sqlKeyWords.split(' ,')
    for i in range(35):
        if sqlkey[i] in text1:
            return False
        if sqlkey[i] in text2:
            return False
        if sqlkey[i] in text4:
            return False
    return True

