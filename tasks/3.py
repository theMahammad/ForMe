# 'Javascript ne vaxtdan proqramlasdirma dili olub?' cumlesinin herf sayini tapin
sentence ='Javascript ne vaxtdan proqramlasdirma dili olub?'
symbols="!?,.$"
for txt in sentence:
    for symbols in symbols:
        if txt==symbols:
            sentence=sentence.replace(txt,"")
        print(len(sentence))