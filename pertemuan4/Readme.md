# RANGKUMAN BAHASA_PEMOGRAMAN


* Tipe data adalah klasifikasi variable untuk menentukan data yang akan disimpan ke dalam memori. Tentunya, berbagai macam tipe data tersebut sangat bermanfaat bagi kinerja komputer melalui kode-kode dalam bahasa pemrograman.

Jenis tipe data yang sering digunakan yaitu Boolean, Character, String, Integer, Floating Point, dan Double Floating Point :
* Boolean
Tipe data Boolean merupakan tipe yang memiliki dua nilai yaitu benar (true) atau salah (false). Nilai yang digunakan pada tipe ini sangat penting dalam mengambil keputusan suatu kejadian tertentu.

* Character
Tipe data character merupakan salah satu tipe data yang memungkinkan kita untuk memesan memori berformat text (huruf, angka, dan simbol) dengan karakter tunggal. Dibutuhkan 1 byte atau 8 bit ruang di dalam memori agar dapat menyimpan sebuah karakter.
* String
Tipe data string terdiri dari kumpulan karakter dengan panjang tertentu, dan seringkali dianggap sebagai tipe data dasar. Hal ini dikarenakan hingga saat ini tipe data string paling sering digunakan oleh para programmer.
* Integer
Jenis tipe data integer dapat didefinisikan sebagai bilangan bulat. Artinya, suatu program yang menggunakan tipe data integer ini tidak mendukung penggunaan huruf. Selain itu, bilangan yang digunakan juga haruslah bulat (tidak mengandung pecahan decimal).
* Floating Point
Tipe data floating point atau real number merupakan tipe data angka yang memiliki bagian decimal di akhir angka. Tipe data float cocok digunakan untuk variable yang akan berisi angka pecahan.
* Double Floating Point
Sama halnya dengan floating point, yang bersifat menyatakan bilangan pecahan. Bedanya adalah penyimpangan angka maksimal lebih besar daripada float, otomatis double juga akan membutuhkan memori yang lebih besar.
* Complex
Sedangkan tipe data numerik yang lainnya adalah tipe data complex, sesuai namanya, ini adalah tipe data yang kompleks. Ia merepresentasikan nilai imajiner.

# RANGKUMAN MODUL 4

penyeleksian if adalah pernyataan penyeleksian yang mencari kebenaran dari conditional
expression yang disebutkan. conditional expression harus berupa
bilangan Boolean atau operasi yang menghasilkan bilangan Boolean dan menyatakan benar
atau salah atas expression tersebut.
Ketika mesin eksekusi bertemu dengan penyeleksian if maka CPU akan memeriksa kebenaran
dari conditional expression yang disebutkan, jika benar (true) maka perintah yang ada di
dalamnya akan dijalankan, jika salah (false) maka akan memeriksa pernyataan else if (jika
ada), hal itu dilakukan berulang satu demi satu hingga menemukan kondisi yang bernilai benar
(true). Jika tidak ditemukan maka akan melakukan perintah pernyataan else. 
Nested IF merupakan hal yang dimungkinkan dalam bahasa pemrograman C++ yaitu membuat
pernyataan IF di dalam pernyataan IF. hal ini dapat memungkinkan anda untuk membuat
tahapan penyeleksian yang berlipat-lipat. Contoh Program :
Pengantar Operasi Penyeleksian 
* Pernyataan percabangan digunakan untuk memecahkan persoalan untuk mengambil suatu keputusan diantara sekian pernyataan yang ada. 
* Dalam bahasa C++ terdapat beberapa perintah, diantaranya adalah :
 * Pernyataan IF 
* Pernyataan IF – ELSE
 * Pernyataan NESTED IF 
* Pernyataan IF – ELSE Majemuk 
* Pernyataan SWITCH - CASE 
Pernyataan IF (lanjutan) 
Cara Pendeklarasian : 
* Penulisan kondisi harus dalam tanda kurung dan berupa ekspresi relasi dan penulisan pernyataan dapat berupa sebuah pernyataan tunggal, pernyataan majemuk atau pernyataan kosong.
* Jika pernyataan IF diikuti dengan pernyataan majemuk, bentuk penulisan sebagai berikut.
Pernyataan IF – ELSE Majemuk (lanjutan)
 • PerSwitch – case merupakan pernyataan yang dirancang khusus untuk menangani pengambilan keputusan yang melibatkan sejumlah atau banyak alternative 
• Pernyataan switch – case memiliki kegunaan yang sama seperti if-else bertingkat, tetapi penggunaannya untuk memeriksa data yang bertipe karakter atau integer
PERBEDAAN IF DAN SWITCH
Flow control (struktur kendali) dapat dibagi menjadi dua jenis yaitu , Struktur percabangan dan pengulangan (looping). Namun kali ini akan membahas struktus percabangan. Percabangan adalah perintah yang memungkinkan pemilihan atas perintah yang akan dijalankan sesuai dengan kondisi tertentu yang menentukan alur perjalanan program.
Ada tiga macam perintah percabangan, yaitu if, if … else, dan switch.
 1. IF If digunakan untuk satu kondisi saja. Jika pernyataan benar (terpenuhi) maka akan dijalankan, jika salah (tidak terpenuhi) maka diabaikan. 
2. IF … ELSE Perintah ini digunakan untuk lebih dari satu kondisi. Seperti biasa, perintah1 dan perintah2 bisa berbentuk blok yang terdiri dari beberapa perintah. Pernyataan if merupakan bentuk percabangan 2 arah, jika kondisi yang diuji tersebut terpenuhi, maka program akan menjalankan pernyataan-pernyataan tertentu.
3. SWITCH Perintah ini digunakan sebagai alternatif pengganti dari sintaks if … else dengan else lebih dari satu. Switch, kondisi hanya dinyatakan dengan bilangan bulat atau karakter/string. Dengan perintah ini program percabangan akan semakin mudah dibuat dan dipelajari. Perintah switch akan menyeleksi kondisi yang diberikan dan kemudian membandingkan hasilnya dengan konstanta-konstanta yang berada di case.
i IF ELSE IF adalah sebuah struktur logika program yang di dapat dengan cara menyambung beberapa kondisi IF ELSE menjadi sebuah kesatuan. Jika kondisi pertama tidak terpenuhi atau bernilai false, maka kode program akan lanjut ke kondisi IF di bawahnya. Jika ternyata tidak juga terpenuhi, akan lanjut lagi ke kondisi IF di bawahnya, dst hingga blok ELSE terakhir atau terdapat kondisi IF yang bernilai true.