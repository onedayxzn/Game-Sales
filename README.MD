# GAME SALES ANALYSIS BY Sukma Ramadhan Asri

## Latar Belakang

    Dataset ini berisi tentang data penjualan game yang diambil dari tahun 1980 hingga 2016. Dataset ini memiliki 11 kolom yang berisi tentang data penjualan game di dunia. Pada data ini dicari informasi tentang game yang paling laris, dan genre game yang paling banyak digemari dan lain sebagainya.

## Question Bussiness

- Specific

  1. Game manakah yang paling laku terjual
  2. Publisher manakah yang paling banyak merilis game
  3. Developer manakah yang paling banyak membuat game
  4. Game yang paling terlama dan terbaru rilis di dalam data ini

- Measurable
  1. Berapa banyak penjualan game terbanyak
  2. Berapa banyak game yang dirilis oleh publisher terbanyak
  3. Berapa banyak game yang dibuat oleh developer terbanyak
  4. Berapa banyak game yang dirilis setiap tahunnya
  5. Series game manakah yang paling banyak penjualannya
  6. Genre game manakah yang paling banyak dibuat/rilis
  7. Genre game manakah yang paling banyak penjualannya

## Data Wrangling

1. cek data

```
game_sales = pd.read_excel(DATA_DIR)
game_sales.head(10)
```

Output

<!-- masukan kode html -->
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sales</th>
      <th>Series</th>
      <th>Release</th>
      <th>Genre</th>
      <th>Developer</th>
      <th>Publisher</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PlayerUnknown's Battlegrounds</td>
      <td>42.0</td>
      <td>NaN</td>
      <td>2017-12-01</td>
      <td>Battle royale</td>
      <td>PUBG Studios</td>
      <td>Krafton</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Minecraft</td>
      <td>33.0</td>
      <td>Minecraft</td>
      <td>2011-11-01</td>
      <td>Sandbox, survival</td>
      <td>Mojang Studios</td>
      <td>Mojang Studios</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Diablo III</td>
      <td>20.0</td>
      <td>Diablo</td>
      <td>2012-05-01</td>
      <td>Action role-playing</td>
      <td>Blizzard Entertainment</td>
      <td>Blizzard Entertainment</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Garry's Mod</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>2006-11-01</td>
      <td>Sandbox</td>
      <td>Facepunch Studios</td>
      <td>Valve</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Terraria</td>
      <td>17.2</td>
      <td>NaN</td>
      <td>2011-05-01</td>
      <td>Action-adventure</td>
      <td>Re-Logic</td>
      <td>Re-Logic</td>
    </tr>
    <tr>
      <th>5</th>
      <td>World of Warcraft</td>
      <td>14.0</td>
      <td>Warcraft</td>
      <td>2004-11-01</td>
      <td>MMORPG</td>
      <td>Blizzard Entertainment</td>
      <td>Blizzard Entertainment</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Half-Life 2</td>
      <td>12.0</td>
      <td>Half-Life</td>
      <td>2004-11-01</td>
      <td>First-person shooter</td>
      <td>Valve</td>
      <td>Valve (digital)</td>
    </tr>
    <tr>
      <th>7</th>
      <td>The Witcher 3: Wild Hunt</td>
      <td>12.0</td>
      <td>The Witcher</td>
      <td>2015-05-01</td>
      <td>Action role-playing</td>
      <td>CD Projekt Red</td>
      <td>CD Projekt</td>
    </tr>
    <tr>
      <th>8</th>
      <td>StarCraft</td>
      <td>11.0</td>
      <td>StarCraft</td>
      <td>1998-03-01</td>
      <td>Real-time strategy</td>
      <td>Blizzard Entertainment</td>
      <td>Blizzard Entertainment</td>
    </tr>
    <tr>
      <th>9</th>
      <td>The Sims</td>
      <td>11.0</td>
      <td>The Sims</td>
      <td>2000-02-01</td>
      <td>Life simulation</td>
      <td>Maxis</td>
      <td>Electronic Arts</td>
    </tr>
  </tbody>
</table>
</div>

2. cek info data

```
game_sales.info()
```

output

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 177 entries, 0 to 176
Data columns (total 7 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   Name       177 non-null    object
 1   Sales      177 non-null    float64
 2   Series     141 non-null    object
 3   Release    177 non-null    datetime64[ns]
 4   Genre      177 non-null    object
 5   Developer  177 non-null    object
 6   Publisher  177 non-null    object
dtypes: datetime64[ns](1), float64(1), object(5)
memory usage: 9.8+ KB
```

Dari data diatas, terdapat 177 baris dan 7 kolom. Kolom tersebut adalah:

- Name: Nama game
- Sales: Penjualan game (dalam Millyaran)
- Series: Nama series game
- Release: Tanggal rilis game
- Genre: Genre game
- Developer: Developer game
- Publisher: Publisher game

jika diperhatikan kolom Series memiliki nilai yang berbeda dengan kolom yang lainnya, hal ini dikarenakan kolom Series memiliki nilai NaN yang berarti tidak ada series game yang dimiliki oleh game tersebut.

3. cek missing value

Untuk mengecek missing value, kita bisa menggunakan fungsi `isna()` dan `sum()` untuk mengetahui jumlah missing value pada kolom Series

```
game_sales.isna().sum()
```

output

```
Name          0
Sales         0
Series       36
Release       0
Genre         0
Developer     0
Publisher     0
```

Dari data diatas, terdapat 36 missing value pada kolom Series, untuk mengatasi missing value tersebut kita bisa mengganti nilai NaN dengan data yang diambil dari kolom Name.

4. mengganti missing value

Untuk mengganti missing value, kita bisa menggunakan fungsi `fillna()` untuk mengganti nilai NaN pada kolom Series dengan data yang diambil dari kolom Name.

```
game_sales['Series'] = game_sales['Series'].fillna(game_sales['Name'])
game_sales.head(10)
```

output

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }

</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Sales</th>
      <th>Series</th>
      <th>Release</th>
      <th>Genre</th>
      <th>Developer</th>
      <th>Publisher</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>PlayerUnknown's Battlegrounds</td>
      <td>42.0</td>
      <td>PlayerUnknown's Battlegrounds</td>
      <td>2017-12-01</td>
      <td>Battle royale</td>
      <td>PUBG Studios</td>
      <td>Krafton</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Minecraft</td>
      <td>33.0</td>
      <td>Minecraft</td>
      <td>2011-11-01</td>
      <td>Sandbox, survival</td>
      <td>Mojang Studios</td>
      <td>Mojang Studios</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Diablo III</td>
      <td>20.0</td>
      <td>Diablo</td>
      <td>2012-05-01</td>
      <td>Action role-playing</td>
      <td>Blizzard Entertainment</td>
      <td>Blizzard Entertainment</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Garry's Mod</td>
      <td>20.0</td>
      <td>Garry's Mod</td>
      <td>2006-11-01</td>
      <td>Sandbox</td>
      <td>Facepunch Studios</td>
      <td>Valve</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Terraria</td>
      <td>17.2</td>
      <td>Terraria</td>
      <td>2011-05-01</td>
      <td>Action-adventure</td>
      <td>Re-Logic</td>
      <td>Re-Logic</td>
    </tr>
    <tr>
      <th>5</th>
      <td>World of Warcraft</td>
      <td>14.0</td>
      <td>Warcraft</td>
      <td>2004-11-01</td>
      <td>MMORPG</td>
      <td>Blizzard Entertainment</td>
      <td>Blizzard Entertainment</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Half-Life 2</td>
      <td>12.0</td>
      <td>Half-Life</td>
      <td>2004-11-01</td>
      <td>First-person shooter</td>
      <td>Valve</td>
      <td>Valve (digital)</td>
    </tr>
    <tr>
      <th>7</th>
      <td>The Witcher 3: Wild Hunt</td>
      <td>12.0</td>
      <td>The Witcher</td>
      <td>2015-05-01</td>
      <td>Action role-playing</td>
      <td>CD Projekt Red</td>
      <td>CD Projekt</td>
    </tr>
    <tr>
      <th>8</th>
      <td>StarCraft</td>
      <td>11.0</td>
      <td>StarCraft</td>
      <td>1998-03-01</td>
      <td>Real-time strategy</td>
      <td>Blizzard Entertainment</td>
      <td>Blizzard Entertainment</td>
    </tr>
    <tr>
      <th>9</th>
      <td>The Sims</td>
      <td>11.0</td>
      <td>The Sims</td>
      <td>2000-02-01</td>
      <td>Life simulation</td>
      <td>Maxis</td>
      <td>Electronic Arts</td>
    </tr>
  </tbody>
</table>
</div>

Dari data diatas, terlihat bahwa kolom Series sudah tidak memiliki nilai NaN lagi. Kita dapat lihat bahwa kolom Series sudah diisi dengan data yang diambil dari kolom Name. contohnya pada kolom ke 1 dengan nama game "PlayerUnknown's Battlegrounds" dan kolom ke 3 dengan nama series "PlayerUnknown's Battlegrounds". Yang awalnya memiliki nilai NaN sekarang sudah diisi dengan nama game tersebut.
