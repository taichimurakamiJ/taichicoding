def get_frequency(file):
    freq={}

    file_data=open(file,encoding="utf-8_sig" )
    for line in file_data:
      words=line.split()

      for word in words:
          word=word.rstrip('].,:!?)’”')
          word=word.lstrip('[(‛“')

          if word in freq:
              freq[word] +=1
          else:
              freq[word]=1

    return freq

#===================================
#　プログラムの起点
#===================================
if __name__  == '__main__':
    file_name =input('ファイル名を入力してください＞＞＞')
    freq = get_frequency(file_name)

for word in sorted(
        freq,
        key=freq.get,
        reverse=True
        ):
         
        word=word.rstrip('].,:!?)’”')
        word=word.lstrip('[(‛“')

        print(
          word + '(' + str(freq[word])+')'
          )
