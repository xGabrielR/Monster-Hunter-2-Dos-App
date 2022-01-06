# Monster Hunter 2 Dos App
<p>This app is a visual product result of web scraping in a monster hunter 2 dos game webpage & pdf's.</p>
<p>Similarly with my other project only in a different game.</p>

![mh2 - Copia](https://user-images.githubusercontent.com/75986085/147991881-691a3e0f-93bc-41af-9af2-3dffe4090952.png)

<h2>1. Business Problem (Objectives)</h2>
 <p>An application that facilitates access to Monster Hunter 2 Dos data, the game is not very popular, due to that there are not many offline quick search tools about the game, check the <a href="https://github.com/xGabrielR/Monster-Hunter-2-Dos-App/blob/main/mh2_database_app_planing.ipynb">App Planning</a> for full info.</p>
 <p>Some data with information of Mh2dos game on jp wiki page or other websites and pdf documents. All information must be easily accessed by the user, Similarly with my other project</p>
 <ul>
    <li>All Quests.</li>
    <li>All Monster.</li>
    <li>All Items.</li>
    <li>All Kitchen Combinations.</li>
    <li>Mix Sets.</li>
</ul>
  
<h2>2. Solution Strategy & Assumptions</h2>
<h3>Assumptions</h3>
<p>The game never get new updates and easy to get data, but some of this data haved a last update on 2012, having some inconsistents.</p>
<h3>First CRISP Cycle</h3>
<ul>
  <dl>
    <dt>Visual Product Design.</dt>
      <dd>The first step is to define the visual product, after some design ideas selected pysimplegui, I opted for pysimplegui to use it more often.</dd>
    <dt>Data Collect.</dt>
      <dd>Used jp and en wiki of monster hunter 2 dos and some pdf documents with data.</dd>
    <dt>Data Cleaning.</dt>
      <dd>Simple regex applications and pandas manipulation using wiki and real game to fill some na or inconsistent values.</dd>
    <dt>Data Storing.</dt>
      <dd>I opted to save the results on sqlite database and csv files for app.</dd>
  </dl>
</ul>
<h2>3. Data Granularity</h2>
<h3>Item Data</h3>
<ul>
  <li>Item Name Granularity.</li>
</ul>
<h3>Monster Data</h3>
<ul>
  <li>Monster Name Granularity.</li>
</ul>
<h3>Recipes Data</h3>
<ul>
  <li>Recipe Effect Granularity.</li>
</ul>
<h3>Quests Data</h3>
<ul>
  <li>Season Granularity.</li>
</ul>
<h2>3. Little Problems Finded</h2>
<p>Some missing data and different tables sizes on wiki and need translation from jp wiki.</p>
