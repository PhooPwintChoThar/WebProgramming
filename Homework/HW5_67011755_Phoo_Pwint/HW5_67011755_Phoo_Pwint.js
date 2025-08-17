function  show_monthOf2025(m_of_year, total_days_of_year){
    var days_of_month=[0,31,28,31,30,31,30,31,31,30,31,30,31];
    if(total_days_of_year==366)
        days_of_month[2]=29;

    var start_days_of_month=[2,0,0,0,0,0,0,0,0,0,0,0,0];
    for(var m=1 ; m<=12; m++ ){
        start_days_of_month[m]=(start_days_of_month[m-1]+days_of_month[m-1])%7;
    }

    var day=1;
    var total_days=days_of_month[m_of_year];
    var month_start_day=start_days_of_month[m_of_year];

    document.writeln("<div><table style='border-collapse:collapse;  margin:auto;'>");
    document.writeln("<thead>");
    document.writeln("<tr> <th style='border: solid 2px black; width:60px; padding: 0;'><button onclick='prevMonth(" + m_of_year + ", " + total_days_of_year + ")'style='background-color: rgb(119, 212, 240); width:100%; height: 100%; border: none; padding: 10px;'>< </button></th> <th colspan='5' style='border: solid 2px black;'>"+m_of_year+"/2025</th> <th style='border: solid 2px black; width:60px; padding: 0;'><button onclick='nextMonth("+m_of_year+","+ total_days_of_year+")' style='background-color: rgb(119, 212, 240); width:100%; height: 100%; border: none; padding: 10px;'>> </button></th> </tr>");
    document.writeln("<tr> <th style='border: solid 2px black; width:60px;'>Mon</th> <th style='border: solid 2px black; width:60px;'>Tue</th> <th style='border: solid 2px black; width:60px;'>Wed</th> <th style='border: solid 2px black; width:60px;'>Thu</th> <th style='border: solid 2px black; width:60px;'>Fri</th> <th style='border: solid 2px black; width:60px;'>Sat</th> <th style='border: solid 2px black; width:60px;'>Sun</th>  </tr>");
    document.writeln("</thead>");
    document.writeln("<tbody><tr>");
      
    for(var blank=0 ; blank<month_start_day; blank++){
        document.writeln("<td style='border: solid 2px black; width:60px; text-align:center;'></td>");
    }
    

    while(day<=total_days){
        document.writeln("<td style='border: solid 2px black; width:60px; text-align:center;'>"+day+"</td>");
        ++day;
        ++month_start_day;
        if(month_start_day>=7 && day<=total_days){
            document.writeln("</tr> \n <tr>");
        }
        month_start_day=month_start_day%7;
    }

    if (month_start_day!=0){
        for(var end=month_start_day ; end<7 ; end++){
         document.writeln("<td style='border: solid 2px black; width:60px; text-align:center;'></td>");
    }

    }
    document.writeln("</tr></tbody>");
    document.writeln("</table></div>");
}

function prevMonth(month, tdays){
    if (month-1==0){
        month=12;
    }else{
        --month;
    }
    document.body.innerHTML="";
    show_monthOf2025(month, tdays);
}

function nextMonth(month, tdays){
    ++month;
    if (month>12){
        month=1;
      }


     document.body.innerHTML="";
     show_monthOf2025(month, tdays);
}

window.addEventListener("load", function() {
    show_monthOf2025(1, 365);
}, false);
