---
toc: true
comments: false
layout: post
title: Sergi's Moto Table
description: This is my personal motorcycle table!
type: hacks
courses: { compsci: {week: 2} }
---

### My Moto Table: 

 <!-- Head contains information to Support the Document -->
<head>
    <!-- load jQuery and DataTables output style and scripts -->
    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script type="text/javascript" language="javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>var define = null;</script>
    <script type="text/javascript" language="javascript" src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
</head>

<!-- Body contains the contents of the Document -->
<body>
    <table id="demo" class="table">
        <thead>
            <tr>
                <th>Make</th>
                <th>Model</th>
                <th>Year</th>
                <th>Color</th>
                <th>Price</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>KTM</td>
                <td>Husqvarna Svartpilen</td>
                <td>2023</td>
                <td>Black</td>
                <td>$5,649</td>
            </tr>
            <tr>
                <td>Piaggio & C. SpA</td>
                <td>Aprilia RS 660</td>
                <td>2023</td>
                <td>Blue</td>
                <td>$11,499</td>
            </tr>
            <tr>
                <td>BMW</td>
                <td>BMW R 1250 GS</td>
                <td>2023</td>
                <td>Gray</td>
                <td>$14,990</td>
            </tr>
            <tr>
                <td>Ducati</td>
                <td>Diavel V4</td>
                <td>2023</td>
                <td>Red</td>
                <td>$26,695</td>
            </tr>
            <tr>
                <td>Honda</td>
                <td>CBR1000RR-R</td>
                <td>2023</td>
                <td>Red</td>
                <td>$19,999</td>
            </tr>
            <tr>
                <td>Suzuki</td>
                <td>GSX-S1000</td>
                <td>2021</td>
                <td>Green</td>
                <td>$11,499</td>
            </tr>
            <tr>
                <td>Kawasaki</td>
                <td>X H2</td>
                <td>2022</td>
                <td>Green</td>
                <td>$17,299</td>
            </tr>
            <tr>
                <td>Yamaha</td>
                <td>MT-10</td>
                <td>2023</td>
                <td>Black</td>
                <td>$14,250</td>
            </tr>
            <tr>
                <td>Indian</td>
                <td>Challenger ELite</td>
                <td>2023</td>
                <td>Blue</td>
                <td>$35,999</td>
            </tr>
            <tr>
                <td>Ducati</td>
                <td>Streetfighter V4</td>
                <td>2020</td>
                <td>Grey</td>
                <td>$21,095</td>
            </tr>
            <tr>
                <td>BMW</td>
                <td>M 1000 RR</td>
                <td>2023</td>
                <td>Black/Blue</td>
                <td>$32,995</td>
            </tr>
            <tr>
                <td>CFMOTO</td>
                <td>Ibex 800 T First</td>
                <td>2023</td>
                <td>Grey</td>
                <td>$9,499</td>
            </tr>
        </tbody>
    </table>
</body>

<!-- Script is used to embed executable code -->
<script>
    $("#demo").DataTable();
</script>



