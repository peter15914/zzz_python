import ftfy

s = r'40.05.01 РџСЂР°РІРѕРІРѕРµ РѕР±РµСЃРїРµС‡РµРЅРёРµ РЅР°С†РёРѕРЅР°Р»СЊРЅРѕР№ Р±РµР·РѕРїР°СЃРЅРѕСЃС‚Рё'

s2 = ftfy.fix_text(s)
print(s2)