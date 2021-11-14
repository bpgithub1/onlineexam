
function GetTodayDate() {
	var date = new Date();
	var currentDate = date.toISOString().substring(0,10);
 return currentDate;
}





/* *********************************************** */

/* this function returns the date(specified) 
 * how to call this Date(YEAR)--> give 2013
 */
function CurrentDate(pFormat){
	var d = new Date();
	var jTmpStr;
	var jInput=pFormat;
	
	var Month=new Array();
		Month[0]="January";
		Month[1]="February";
		Month[2]="March";
		Month[3]="April";
		Month[4]="May";
		Month[5]="June";
		Month[6]="July";
		Month[7]="August";
		Month[8]="September";
		Month[9]="October";
		Month[10]="November";
		Month[11]="December";
		
	var Mon=new Array();
		Mon[0]="Jan";
		Mon[1]="Feb";
		Mon[2]="Mar";
		Mon[3]="Apr";
		Mon[4]="May";
		Mon[5]="Jun";
		Mon[6]="Jul";
		Mon[7]="Aug";
		Mon[8]="Sep";
		Mon[9]="Oct";
		Mon[10]="Nov";
		Mon[11]="Dec";
	
	if(jInput==='YEAR'||jInput==='Year'||jInput==='year'||jInput==='YYYY'||jInput==='Y'){
		jTmpStr=d.getFullYear();
	}else if(jInput==='MM'||jInput==='M'){
		jTmpStr=d.getMonth()+1;
	}else if(jInput==='MONTH'||jInput==='Month'||jInput==='month'){
		jTmpStr=Month[d.getMonth()];
	}else if(jInput==='MON'||jInput==='Mon'||jInput==='mon'){
		jTmpStr=Mon[d.getMonth()];
	}else if(jInput==='DAY'||jInput==='Day'||jInput==='day'||jInput==='DD'||jInput==='D'){
		jTmpStr=d.getDate();
	}else if(jInput==='Dd-Mon-Yyyy'||jInput==='dd-mon-yyyy'||jInput==='DD-MON-YYYY') {
		jTmpStr=d.getDate()+"-"+Mon[d.getMonth()]+"-"+d.getFullYear();
	} else {
		jTmpStr='Unknown Date Format';
	}
	
	return jTmpStr;
}

/* Extract Year , Month ,Day from given input date in the format of 'Dd-Mon-YYYY'
 *
 */
function ExtractDay(pDateStr){
	var jDateStr=pDateStr;
	//var jTmpStr;
	return(jDateStr.substring(0, 2));
}
function ExtractMonth(pDateStr){
	var jDateStr=pDateStr;
	//var jTmpStr;
	return(jDateStr.substring(3, 6));
}
function ExtractYear(pDateStr){
	var jDateStr=pDateStr;
	//var jTmpStr;
	return(jDateStr.substring(7, 11));
}
function ExtractMM(pDateStr){
	var jDateStr=pDateStr;
	var jTmpStr;
	jTmpStr=jDateStr.substring(3, 6);
	if(jTmpStr==='Jan'){
		return 1;
	}else if(jTmpStr==='Feb'){
	    return 2;
	}else if(jTmpStr==='Mar'){
	    return 3;
	}else if(jTmpStr==='Apr'){
	    return 4;
	}else if(jTmpStr==='May'){
	    return 5;
	}else if(jTmpStr==='Jun'){
	    return 6;
	}else if(jTmpStr==='Jul'){
	    return 7;
	}else if(jTmpStr==='Aug'){
	    return 8;
	}else if(jTmpStr==='Sep'){
	    return 9;
	}else if(jTmpStr==='Oct'){
	    return 10;
	}else if(jTmpStr==='Nov'){
	    return 11;
	}else if(jTmpStr==='Dec'){
	    return 12;
	}
	/////
	if(jTmpStr==='JAN'){
		return 1;
	}else if(jTmpStr==='FEB'){
	    return 2;
	}else if(jTmpStr==='MAR'){
	    return 3;
	}else if(jTmpStr==='APR'){
	    return 4;
	}else if(jTmpStr==='MAY'){
	    return 5;
	}else if(jTmpStr==='JUN'){
	    return 6;
	}else if(jTmpStr==='JUL'){
	    return 7;
	}else if(jTmpStr==='AUG'){
	    return 8;
	}else if(jTmpStr==='SEP'){
	    return 9;
	}else if(jTmpStr==='OCT'){
	    return 10;
	}else if(jTmpStr==='NOV'){
	    return 11;
	}else if(jTmpStr==='DEC'){
	    return 12;
	}
	/////
	if(jTmpStr==='jan'){
		return 1;
	}else if(jTmpStr==='feb'){
	    return 2;
	}else if(jTmpStr==='mar'){
	    return 3;
	}else if(jTmpStr==='apr'){
	    return 4;
	}else if(jTmpStr==='may'){
	    return 5;
	}else if(jTmpStr==='jun'){
	    return 6;
	}else if(jTmpStr==='jul'){
	    return 7;
	}else if(jTmpStr==='aug'){
	    return 8;
	}else if(jTmpStr==='sep'){
	    return 9;
	}else if(jTmpStr==='oct'){
	    return 10;
	}else if(jTmpStr==='nov'){
	    return 11;
	}else if(jTmpStr==='dec'){
	    return 12;
	}
}


//calling jsp must use form tag
function SubmitForm(pUrl){
    reqSubmittedFlag = true;
    document.forms[0].action = pUrl;
    document.forms[0].submit();
}  


/* round up to two decimals */
function RoundTwoDecimals(pNumber){
  return(Math.round(pNumber*100)/100);
}
/* round up to Zero decimals */
function RoundZeroDecimals(pNumber){
  return(Math.round(pNumber));
}

// this function pads the gievn numbers of zeros to left of an input numeric value  
function LeftPadZeros(pNumber, pLength) {
    var jStrNumber = '' + pNumber; // to convert number into string
    var jLength=pLength;
    while (jStrNumber.length < jLength) {
        jStrNumber = '0' + jStrNumber;
    }
    return jStrNumber;
}

//User Customized PopUp
function PopUpWindow(pUrl,pWidth,pHeight){
   newwindow=window.open(pUrl,'CustomPopUpWindow','width='+pWidth,'height='+pHeight,'toolbar=no,location=no,directories=no,status=no, menubar=no,scrollbars=yes,resizable=yes,addressbar=no');  
}
//self explanatory
function ConfirmDelete(){
	var msg=confirm("Do you want to delete ?");
	if(msg){
		return true;			
	}else{
		return false;
	}
}	
//based on index this function will return the "Keywords" ;
//this function is used to conver amount in words in fucntion "AmountInWords" function 
function GetWord(pIndx){
    var WordList=new Array();
    WordList[0] = "Zero";
	WordList[1] = "One";
	WordList[2] = "Two";
	WordList[3] = "Three";
	WordList[4] = "Four";
	WordList[5] = "Five";
	WordList[6] = "Six";
	WordList[7] = "Seven";
	WordList[8] = "Eight";
	WordList[9] = "Nine";
	WordList[10] = "Ten";
	WordList[11] = "Eleven";
	WordList[12] = "Twelve";
	WordList[13] = "Thirteen";
	WordList[14] = "Fourteen";
	WordList[15] = "Fifteen";
	WordList[16] = "Sixteen";
	WordList[17] = "Seventeen";
	WordList[18] = "Eighteen";
	WordList[19] = "Nineteen";
	WordList[20] = "Twenty";
	WordList[21] = "Twenty One";
	WordList[22] = "Twenty Two";
	WordList[23] = "Twenty Three";
	WordList[24] = "Twenty Four";
	WordList[25] = "Twenty Five";
	WordList[26] = "Twenty Six";
	WordList[27] = "Twenty Seven";
	WordList[28] = "Twenty Eight";
	WordList[29] = "Twenty Nine";
	WordList[30] = "Thirty";
	WordList[31] = "Thirty One";
	WordList[32] = "Thirty Two";
	WordList[33] = "Thirty Three";
	WordList[34] = "Thirty Four";
	WordList[35] = "Thirty Five";
	WordList[36] = "Thirty Six";
	WordList[37] = "Thirty Seven";
	WordList[38] = "Thirty Eight";
	WordList[39] = "Thirty Nine";
	WordList[40] = "Forty";
	WordList[41] = "Forty One";
	WordList[42] = "Forty Two";
	WordList[43] = "Forty Three";
	WordList[44] = "Forty Four";
	WordList[45] = "Forty Five";
	WordList[46] = "Forty Six";
	WordList[47] = "Forty Seven";
	WordList[48] = "Forty Eight";
	WordList[49] = "Forty Nine";
	WordList[50] = "Fifty";
	WordList[51] = "Fifty One";
	WordList[52] = "Fifty Two";
	WordList[53] = "Fifty Three";
	WordList[54] = "Fifty Four";
	WordList[55] = "Fifty Five";
	WordList[56] = "Fifty Six";
	WordList[57] = "Fifty Seven";
	WordList[58] = "Fifty Eight";
	WordList[59] = "Fifty Nine";
	WordList[60] = "Sixty";
	WordList[61] = "Sixty One";
	WordList[62] = "Sixty Two";
	WordList[63] = "Sixty Three";
	WordList[64] = "Sixty Four";
	WordList[65] = "Sixty Five";
	WordList[66] = "Sixty Six";
	WordList[67] = "Sixty Seven";
	WordList[68] = "Sixty Eight";
	WordList[69] = "Sixty Nine";
	WordList[70] = "Seventy";
	WordList[71] = "Seventy One";
	WordList[72] = "Seventy Two";
	WordList[73] = "Seventy Three";
	WordList[74] = "Seventy Four";
	WordList[75] = "Seventy Five";
	WordList[76] = "Seventy Six";
	WordList[77] = "Seventy Seven";
	WordList[78] = "Seventy Eight";
	WordList[79] = "Seventy Nine";
	WordList[80] = "Eighty";
	WordList[81] = "Eighty One";
	WordList[82] = "Eighty Two";
	WordList[83] = "Eighty Three";
	WordList[84] = "Eighty Four";
	WordList[85] = "Eighty Five";
	WordList[86] = "Eighty Six";
	WordList[87] = "Eighty Seven";
	WordList[88] = "Eighty Eight";
	WordList[89] = "Eighty Nine";
	WordList[90] = "Ninety";
	WordList[91] = "Ninety One";
	WordList[92] = "Ninety Two";
	WordList[93] = "Ninety Three";
	WordList[94] = "Ninety Four";
	WordList[95] = "Ninety Five";
	WordList[96] = "Ninety Six";
	WordList[97] = "Ninety Seven";
	WordList[98] = "Ninety Eight";
	WordList[99] = "Ninety Nine";
	WordList[100] = "One Hundred";
	return WordList[pIndx];
} 
// this function will convert the amount into words in Indian Standards 
function AmountInWords(pAmt){ 
  var FinalStr="";        
  if(pAmt>999999999.99){
      //If number is grater than 99 crore then do not convert to words from numeric 
  }else{
   var vAmt;
   vAmt=pAmt+"";//this will convert number to string  
   var Numeric,Decimal,DecimalsInWords="",NumericInWords="";
   //-----For Numeric Part-----------//
   if(vAmt.indexOf(".", 0)==-1) //this means no decimals
   {
      //Do nothing; numeric field become remain numeric, jsut assign
      Numeric=vAmt;
   }else{
     Numeric=vAmt.slice(0,vAmt.indexOf(".", 0));
   }      
   Numeric=Numeric.lpad("0", 9);
   //Check at Crore position;
   if(Numeric.substr(0,1)=="0" && Numeric.substr(1,1)=="0"){   
   }else{ 
     if(Numeric.substr(0,1)=="0"){
       NumericInWords=GetWord(Numeric.substr(1,1))+" Crore ";
     }else{
       NumericInWords=GetWord(Numeric.substr(0,2))+" Crore ";
     }      
   }
   //Check at Lac position;
   if(Numeric.substr(2,1)=="0" && Numeric.substr(3,1)=="0"){   
   }
   else{ 
     if(Numeric.substr(2,1)=="0"){
       NumericInWords=NumericInWords+GetWord(Numeric.substr(3,1))+" Lac ";
     }else{
       NumericInWords=NumericInWords+GetWord(Numeric.substr(2,2))+" Lac ";
     }       
   }
   //Check at Thousand position;
   if(Numeric.substr(4,1)=="0" && Numeric.substr(5,1)=="0"){   
   }else{ 
     if(Numeric.substr(4,1)=="0"){
       NumericInWords=NumericInWords+GetWord(Numeric.substr(5,1))+" Thousand ";
     }else{
       NumericInWords=NumericInWords+GetWord(Numeric.substr(4,2))+" Thousand ";
     }       
   }
   //Check at Hundred position;
   if(Numeric.substr(6,1)=="0"){   
   }else{ 
     NumericInWords=NumericInWords+GetWord(Numeric.substr(6,1))+ " Hundred ";            
   }
   //Check at Thousand position;
   if(Numeric.substr(7,1)=="0" && Numeric.substr(8,1)=="0"){   
   }else{ 
     if(Numeric.substr(7,1)=="0"){
       NumericInWords=NumericInWords+GetWord(Numeric.substr(8,1));
     }else{
       NumericInWords=NumericInWords+GetWord(Numeric.substr(7,2));
     }      
   }
   //-----For Decimal Part-----------//
   if(vAmt.indexOf(".", 0)==-1) //this means no decimals
   {
      DecimalsInWords=GetWord(0);
   }else{
     Decimal=vAmt.slice(vAmt.indexOf(".", 0)+1,vAmt.length);
   	 Decimal=Decimal.rpad("0", 2);  
   	 if(Decimal.substr(0,1) == "0" ) // this will work for 01,02, ,.. , 09
   	 {
   	   Decimal=Decimal.substr(1,1);
   	 }  
   	 DecimalsInWords=GetWord(Decimal);   
   }
   //-----Combining Numeric and Decimal Part-----------//
   if(NumericInWords==""){
     NumericInWords="Zero";
   }
   FinalStr=NumericInWords+" Rs And "+ DecimalsInWords +" Paise";
  } 
  return  FinalStr; 
   
}


//this function separates the given amount with comma
/* 
 * assumption is to display comma separated till 99,99,99,999.00
 * suppose we have 999999999.00; before calling this function separate 999.00(as this need not to separate as comma) 
 * and pass 999999 only to this  then this function will return 99,99,99.
 */
function AmountWithComma(pAmount){
	var jCommaHolder=new Array();
	jCommaHolder[0]='';
	jCommaHolder[1]='';
	jCommaHolder[2]=',';
	jCommaHolder[3]='';
	jCommaHolder[4]='';
	jCommaHolder[5]=',';
	jCommaHolder[6]='';
	jCommaHolder[7]='';
	jCommaHolder[8]=',';
	
	var jAmount=pAmount;
	var FinalStr="";  
	var i=0,k=0;
	k=jCommaHolder.length-1;
	for (i=jAmount.length-1;i>=0;i--){
		if(jCommaHolder[k]==","){
			k--;			
		}
		jCommaHolder[k]=jAmount[i];	
		k--;		
	}
	
	for(i=0;i<jCommaHolder.length;i++){
		FinalStr=FinalStr+jCommaHolder[i];
	}
	
	for (i=0;i<FinalStr.length;i++){
        if(FinalStr[i]==','){                    
        }else {
               FinalStr=FinalStr.substring(i,FinalStr.length);
               break;
        }      
    }
    return  FinalStr;      
} 

function AmountValidateMaxLength(pAmount){
	var jAmountLength=pAmount.length;
	if(jAmountLength>14){
		//alert("Amount Limit Exceeded (max 14 digit allowed) !");
		return true;
	}else{
		return false;
	}
}


//Below two function are from google for paddng the string. 
//pads left
String.prototype.lpad = function(padString, length) {
	var str = this;
    while (str.length < length)
        str = padString + str;
    return str;
};
//pads right
String.prototype.rpad = function(padString, length) {
	var str = this;
    while (str.length < length)
        str = str + padString;
    return str;
};
//trim function is available in all latest browser if not available then this function will be used to trim
//otherwise inbuilt trim function will be used
if (!String.prototype.trim) {
	 String.prototype.trim = function() {
	  return this.replace(/^\s+|\s+$/g,'');
	 };
}
//
function IsEnterPressed(e){
    var keynum="";
	//var keychar;
	//var numcheck;
    if(window.event){ 		// IE8 and earlier                
		keynum = e.keyCode;                
	}else if(e.which){ 		// IE9/Firefox/Chrome/Opera/Safari                
		keynum = e.which;               
	}
	if (keynum == 13){                                          
		return true;		
	}
	else{
		return false;
	}
}

//
function ShowMe(pElement){     
     document.getElementById(pElement).style.visibility="visible";
}

//
function HideMe(pElement){
     document.getElementById(pElement).style.visibility="hidden";
}

/* this function will create a 2-D array if calling function passes no of rows , no of columns*/
function Create2DArray(pRow,pCol){ 
  var iMax = pRow;
  var jMax = pCol;
  var TmpArr = new Array();
  for (var i=0;i<iMax;i++) {
   TmpArr[i]=new Array();
    for (var j=0;j<jMax;j++) {
     TmpArr[i][j]=j;
    }
  }
  return TmpArr;  
 }
/* --------------------Matrix Functions---------------------   */
/* 	Both ReportMatrix & LinkMatrix function are similar in nature 
	the difference is only that in LinkMatrix the first column will become given pLink with fist column value as input
	ReportMatrix could be used in reports where are LinkMatrix can be used to show search results. 
*/
 
//This function will display 2d-matrix on the page based on parameter
//paramerets are : pTable Name -	on page where to display , like div name or table name
//				   pCols -			no of columns
//				   pRows -			no of rows
//				   pMatrixValue - 	a 2d array for values to be display
//for better dispaly always keep the first row as header
//This function is used to explore i.e. showing search results at any place
 

//This function will display 2d-matrix on the page based on parameter
//paramerets are : pTable Name -	on page where to display , like div name or table name
//				   pCols -			no of columns
//				   pRows -			no of rows
//				   pValueMatrix - 	a 2d array for values to be display
//for better dispaly always keep the first row as header
//This function is used to explore i.e. showing search results at any place
//this is a dead link matrix because href does not forward to any page
 
/* -----------------------------------------   */
//This function will display 2d-matrix on the page based on parameter
//paramerets are : pTable Name -	on page where to display , like div name or table name
//				   pCols -			no of columns
//				   pRows -			no of rows
//				   pValueMatrix - 	a 2d array for values to be display
//for better dispaly always keep the first row as header
//This function is used to explore i.e. showing search results at any place
//this is a Link link matrix because href forward to given page
 
/* -----------------------------------------   */
/* this function will extract the sub string from match onwards to end of input strings */

       function ExtractString(pStr,pMatch){
              var jStr=""+pStr;
              var jMatch=""+pMatch;
              var from=jStr.search(jMatch)+1;
              var to=jStr.length;
              var jSubStr=jStr.substring(from, to);
              return jSubStr;
       }
/* -----------------------------------------   */
/* this function sets the given radio value to a given target elements like textbox or hidden elements */
//how to call this function SetRadioValue(RadioId,TargetObjectId)
function SetRadioValue(pSourceRadioObj,pTargetAnyObj){
	var jS=pSourceRadioObj;
	var jT=pTargetAnyObj;			
	var jStr=$(jS).val();
	var jElement=document.getElementById(jT);
	jElement.value=jStr;	
	return true;			    		
}

/* -----------------------------------------   */
/* this function gives the selected radio value */
function GetRadioValue(pRadioName){ 
	var vRadioVal="";	
   for (var i=0; i<document.forms[0][pRadioName].length; i++){
     if (document.forms[0][pRadioName][i].checked){
        vRadioVal = document.forms[0][pRadioName][i].value;            
      }
    }
   return vRadioVal;
}
 
/* this function check(tick) the radio button using passed value */
function CheckRadio(pRadioName,pValue){   
   for (var i=0; i<document.forms[0][pRadioName].length; i++){
     vRadioVal = document.forms[0][pRadioName][i].value; 
     if (vRadioVal===pValue){
     	document.forms[0][pRadioName][i].checked=true;
     	break;                 
      }
    }
   return true;
}
 
/* this function check(tick) the radio button using passed value */
function CheckRadio_New(pForm,pRadioName,pValue){   
   for (var i=0; i<document.forms[pForm][pRadioName].length; i++){
     vRadioVal = document.forms[pForm][pRadioName][i].value; 
     if (vRadioVal===pValue){
     	document.forms[pForm][pRadioName][i].checked=true;
     	break;                 
      }
    }
   return true;
}
/* 	
	* this function will populate the given select box id (pSelectBoxId) 
	* with 2d-Matrix values (pValueMatrix); 
*/
     function PopulateSelectBox(pSelectBoxId,pValueMatrix){
            var jSelect = document.getElementById(pSelectBoxId);
            document.getElementById(pSelectBoxId).options.length = 0;
            for(var i=0;i<pValueMatrix.length;i++){
                  var jOption=document.createElement('option');
                  var jValue=pValueMatrix[i][0];
                  var jDesc=pValueMatrix[i][1];
                  jOption.setAttribute('value',jValue);
                  jOption.appendChild(document.createTextNode(jDesc));
                  jSelect.appendChild(jOption);
            }
            jSelect.selectedIndex=0;
            
     }
              
/* this function will highlight the given select box id (pSelectBoxId) with given values (pValue); */
     function HighlightSelectBox(pSelectBoxId,pValue){
            var jSelectObj=document.getElementById(pSelectBoxId);
            var jText;
            var jValue;
            for (var i=0; i<jSelectObj.length; i++){
                  jText=jSelectObj.options[i].text;
                  jValue=jSelectObj.options[i].value;
                  if(jValue==pValue ||jText==pValue){                                  
                         jSelectObj.selectedIndex=i;
                         break;
                  }else {
                         jSelectObj.selectedIndex=-1;
                  }
                  
            }
     }
 
	/* 
     * Retrieve Reference Values from database for given RefKey 
     * Return type of this function is 2-d Array; 
     * Internally this function takes the help of Create2DArray() function to return 2-d Array 
     * the returned 2-d array can be passed in PopulateSelectBox() to populate select box
     * then use HighlightSelectBox() to highlight specific values
     * pRefKey -> which reference to pick
     * pSelectBoxId -> select box where values to be filled in from database
     * pMarker -> highlight the particular value after drop down is populated.
     */           
      function FillDropDownReference(pRefKey,pSelectBoxId,pMarker) {    
      	$.ajax({  
            type: "GET",  
            url: "CommonFillDropDownReference.do", 
            dataType:"json", 
            cache:false,
            async:false,
            data: "exploreKey=" + pRefKey,  
            //data: { "exploreKey":TmpStr, "userId":"R249766" },   //how to populate form bean
            success: function(response){   
               		var Records=0;
            		$.each(response, function(i, employeeId){               
               			Records=parseInt(i)+1;
            		});
		            if (response[0]==='Session Expired'){
		               //alert("Session Expired !");	
		               //SubmitForm('SessionExpire.do');		               
		            } else { 
		               var i=parseInt(0),j=parseInt(0);//,k=parseInt(0);
		               var Tmp2dArray=Create2DArray(Records,2);// Records --> No of rows, 2--> no of colums // user defined function
		               var jCode="";
		               var jDesc="";
		               for (i=0;i<Records;i++){
		                   j=parseInt(0);                           
		                   //reading values from response and assigning to variables                                       
		                   jCode=response[i].code;
		                   jDesc=response[i].desc;
		                   //filling arrays using above assigned values from response.                                        
		                   Tmp2dArray[i][j++]=jCode;
		                   Tmp2dArray[i][j++]=jDesc;                                                                                                                                              
		               }             
		               PopulateSelectBox(pSelectBoxId,Tmp2dArray);
		               HighlightSelectBox(pSelectBoxId,pMarker);                                           
		           }           
		          },  
          error: function(e){  
                 alert('AJAX Error Occured:' + e);
		    	 SubmitForm('Error.do');
                 
          }  
      }); 
             
	}

      /* 
       * Retrieve Customer ID & Name from database for populating Drop Down 
       * Return type of this function is 2-d Array; 
       * Internally this function takes the help of Create2DArray() function to return 2-d Array 
       * the returned 2-d array can be passed in PopulateSelectBox() to populate select box
       * then use HighlightSelectBox() to highlight specific values
       * pSelectBoxId -> select box where values to be filled in from database
       * pMarker -> highlight the particular value after drop down is populated.
       */           
        function FillDropDownCustomer(pSelectBoxId,pMarker) {    
        	$.ajax({  
              type: "GET",  
              url: "CommonFillDropDownCustomer.do", 
              dataType:"json", 
              cache:false,
              async:false,
              //data: "exploreKey=" + pRefKey,  
              //data: { "exploreKey":TmpStr, "userId":"R249766" },   //how to populate form bean
              success: function(response){   
                 		var Records=0;
              		$.each(response, function(i, employeeId){               
                 			Records=parseInt(i)+1;
              		});
  		            if (response[0]==='Session Expired'){
  		               //alert("Session Expired !");	
  		               //SubmitForm('SessionExpire.do');		               
  		            } else { 
  		               var i=parseInt(0),j=parseInt(0);//,k=parseInt(0);
  		               var Tmp2dArray=Create2DArray(Records,2);// Records --> No of rows, 2--> no of colums // user defined function
  		               var jCode="";
  		               var jDesc="";
  		               for (i=0;i<Records;i++){
  		                   j=parseInt(0);                           
  		                   //reading values from response and assigning to variables                                       
  		                   jCode=response[i].customerId;
  		                   jDesc=response[i].customerName;
  		                   //filling arrays using above assigned values from response.                                        
  		                   Tmp2dArray[i][j++]=jCode;
  		                   Tmp2dArray[i][j++]=jDesc;                                                                                                                                              
  		               }             
  		               PopulateSelectBox(pSelectBoxId,Tmp2dArray);
  		               HighlightSelectBox(pSelectBoxId,pMarker);                                            
  		           }           
  		          },  
            error: function(e){  
                   alert('AJAX Error Occured:' + e);
  		    	   SubmitForm('Error.do');
                   
            }  
        }); 
               
  	}    
        
        /* 
         * Retrieve Shipment ID & No from database for populating Drop Down 
         * Return type of this function is 2-d Array; 
         * Internally this function takes the help of Create2DArray() function to return 2-d Array 
         * the returned 2-d array can be passed in PopulateSelectBox() to populate select box
         * then use HighlightSelectBox() to highlight specific values
         * pSelectBoxId -> select box where values to be filled in from database
         * pMarker -> highlight the particular value after drop down is populated.
         */           
          function FillDropDownShipment(pSelectBoxId,pMarker,pShipmentType) {    
          	  $.ajax({  
                type: "GET",  
                url: "CommonFillDropDownShipment.do", 
                dataType:"json", 
                cache:false,
                async:false,
                data: { 
                		"exploreKey":pShipmentType, 
                	  }, 
                success: function(response){   
                   		var Records=0;
                		$.each(response, function(i, employeeId){               
                   			Records=parseInt(i)+1;
                		});
    		            if (response[0]==='Session Expired'){
    		               //alert("Session Expired !");	
    		               //SubmitForm('SessionExpire.do');		               
    		            } else { 
    		               var i=parseInt(0),j=parseInt(0);//,k=parseInt(0);
    		               var Tmp2dArray=Create2DArray(Records,2);// Records --> No of rows, 2--> no of colums // user defined function
    		               var jCode="";
    		               var jDesc="";
    		               for (i=0;i<Records;i++){
    		                   j=parseInt(0);                           
    		                   //reading values from response and assigning to variables                                       
    		                   jCode=response[i].shipId;
    		                   jDesc=response[i].shipNumber;
    		                   //filling arrays using above assigned values from response.                                        
    		                   Tmp2dArray[i][j++]=jCode;
    		                   Tmp2dArray[i][j++]=jDesc;                                                                                                                                              
    		               }             
    		               PopulateSelectBox(pSelectBoxId,Tmp2dArray);
    		               HighlightSelectBox(pSelectBoxId,pMarker);                                            
    		           }           
    		          },  
              error: function(e){  
                     alert('AJAX Error Occured:' + e);
    		    	   SubmitForm('Error.do');
                     
              }  
          }); 
                 
    	}   
/*
 *  this function returns all the ids of textboxes presentin in a page; return type is an 1d-array
 */
function ListTextBoxes(){
    var jElement = document.getElementsByTagName('input');
    var jTxtBoxList=[];
    var j=0;
    for(var i=0; i<jElement.length; i++){
          if(jElement[i].type=='text'||jElement[i].type=='password'){
                 jTxtBoxList[j++]=jElement[i].id;
          }             
    }      
    return jTxtBoxList;
}  

/*
 * this function receives 2-d array with 2 columns 
 * whose first column is the name of the HTML elements
 * and the second column is the alert message you want to show 
 * this function returns TRUE if any elements of the array is emplty
 * if no text box is empty then returns FALSE
 */
function EmptyBoxAlertUnique(p2DArray){
   var jTmpArray=p2DArray;
   var jRows=jTmpArray.length;
   for(var i=0;i<jRows;i++){
          var jElement=document.getElementById(jTmpArray[i][0]);
          if(jElement.value==null||jElement.value==""||jElement.value==''){             
                 alert(jTmpArray[i][1]+" is empty !");
              return true;
          }             
   }
   return false;     
}		
/*
 *  this function receives 1-d array  of text box IDs  
 *  this function returns TRUE if any elements of the array is emplty
 *  if no text box is empty then returns FALSE
 *  limitation of this function is that alert messages can't be generated separately
 */
function EmptyBoxAlertSame(pTxtBxList){
   var jTmpArray=pTxtBxList;
   var jRows=jTmpArray.length;
   for(var i=0;i<jRows;i++){
     var jElement=document.getElementById(jTmpArray[i]);
     if(jElement.value==null||jElement.value==""||jElement.value==''){             
         alert(jTmpArray[i]+" is empty !");
         return true;
     }             
   }
   return false;     
}
/* this function returns true if non alpha numeric charachter found */            
function IsAlphaNumeric(pStr){
	var jStr = pStr;
    for(var i=0; i<jStr.length; i++){
       var jChar = jStr.charAt(i);
       var jCharCode = jChar.charCodeAt(0);
       if((jCharCode>47 && jCharCode<58) || (jCharCode>64 && jCharCode<91) || (jCharCode>96 && jCharCode<123)){
		///----
       }else {
			return true; 
       }
	}
	  return false;   
}

/*
* this function directly just convert amount into comma separated
* used in reports across 
*/
function CommaSeparatedAmount(pAmount){      
          var jAmount=pAmount;
          var jAmountDecimal= parseFloat(jAmount).toFixed(2);
          
          if(jAmount.length<13){
        	  var jStr1=jAmountDecimal.substring(0,jAmountDecimal.length-6); //first (n-6) digit; needed to separate as comma
              var jStr2=jAmountDecimal.slice(-6); //last 6 digit; not needed to separate as comma
              var jStr;
              if(jStr1.length>0){
                     jStr=AmountWithComma(jStr1)+jStr2;
              }else{
                     jStr=jStr2;
              }
              return jStr;              
          }   
}


/*
	* this function is only to display on page,
	* pShowComma - span to show comma separated amounts
	* pShowWord - abbreviation tag to display amount in words
	* pShowHomeCcy - span to display Home Currecny    
	* pCcy - Home Currency Value
	* pAmount - Amount to be comma separated
	* how to call this function eg: DisplayAmount('spanComma','abbrWord','spanCcy',123456789,'INR');
*/
function DisplayAmountHome(pShowComma,pShowWord,pShowHomeCcy,pAmount,pCcy){      
              var jComma=document.getElementById(pShowComma);
              var jWords=document.getElementById(pShowWord); 
              var jHomeCcy=document.getElementById(pShowHomeCcy); 
              //var jAmount=document.getElementById(pAmount).value;
              var jAmount=pAmount;
              var jCcy=pCcy;
              var jAmountDecimal= parseFloat(jAmount).toFixed(2);
              
              if(jAmount.length<13){
            	  var jStr1=jAmountDecimal.substring(0,jAmountDecimal.length-6); //first (n-6) digit; needed to separate as comma
	              var jStr2=jAmountDecimal.slice(-6); //last 6 digit; not needed to separate as comma
	              var jStr;
	              if(jStr1.length>0){
	                     jStr=AmountWithComma(jStr1)+jStr2;
	              }else{
	                     jStr=jStr2;
	              }
	              jComma.innerHTML=jStr;
	              jHomeCcy.innerHTML=jCcy;
	              jWords.title=AmountInWords(jAmountDecimal);
              }else{
            	  if(jAmount.length>=13 && jAmount.length<=14){
            		 jComma.innerHTML=jAmount;
    	             jHomeCcy.innerHTML=jCcy;
    	             jWords.title=jAmountDecimal;  
            	  }else{
            		  if(AmountValidateMaxLength(jAmount)==true){
            			 jComma.innerHTML="";
         	             jHomeCcy.innerHTML=jCcy;
         	             jWords.title=""; 
            		  } 
            	  }
            	   
              }    
    }

  /* 
	 * pLoc			: location where grid to be place div/table id
	 * pCols		: no of columns in grid
	 * pRows		: no of rows in grid
	 * pColHeader	: an array of header display for the grid
	 * pColName 	: an array of the name of the each columns of grid
	 * this function create a grid at given location; 
	 * how to call this function e.g.
	 * var header=['Employee Id','Employee Name','Employee Address'];
	 * var name=['id','name','address'];
	 * CreateGrid('grid',3,5,header,name);
	 * ===currently not used in this project; it is for future use======
	 */
	function CreateGrid_xx(pLoc,pCols,pRows,pColHeader,pColName){
		var jLoc=pLoc;
		var jCols=pCols;
		var jRows=pRows;
		var jColHeader=pColHeader;
		var jColName=pColName;
		var jHeaderCount=jColHeader.length;
		var jColCount=jColName.length;
		if(jHeaderCount!=jColCount){
			alert("Grid Header & Column Length; Mismatched !");
		}else if(jHeaderCount!=jCols){
			alert("Grid Header/Column Length & No Of Columns Provided; Mismatched !");
		}else{
			///////////////////
		    var root=document.getElementById(jLoc);
			var tab=document.createElement('table');
			tab.className="mytable";
			var tbo=document.createElement('tbody');
			var row, cell;
			for(var i=0;i<jRows;i++)
			{
				row=document.createElement('tr');
				row.style.backgroundColor = "#D2B48C";
				for(var j=0;j<jCols;j++){
				    if(i===0){
				    	row.style.backgroundColor = "#4C1A00"; 
				    	row.style.color = "#FFFFCC"; 
						cell=document.createElement('th');
				    	cell.innerHTML=jColHeader[j];
				    	row.appendChild(cell);					    	
				    }else{
				    	cell=document.createElement('td');
				    	var a = document.createElement('input');
				    	a.type = "text";
				        a.name=jColName[j]; 
				        a.style.border="0px";
				        cell.appendChild(a);
						row.appendChild(cell);
				    }						
				}
				tbo.appendChild(row);
			}
			tab.appendChild(tbo);
			root.appendChild(tab);			 
			//////////////////			
		}
	} 
	//This function will check whether a input text box is having a valid number or not
	//according to the business requirement negatives are considered as invalid Numbers
	function IsNumber(pInputValue){
	   var strValidChars = "-0123456789.";
	   var strChar;
	   var blnResult = true;
	   var TxtBxVal=pInputValue;                
	   var Flag=isNaN(TxtBxVal);
	   if(Flag){
	     blnResult = false;
	   }else if(TxtBxVal.charAt(TxtBxVal.length-1)=="."){
	     blnResult = false;
	   }else{
		   for (var i = 0; i < TxtBxVal.length && blnResult == true; i++){
		      strChar = TxtBxVal.charAt(i);
		      if (strValidChars.indexOf(strChar) == -1){
		           blnResult = false;
		         }
		    }
	   }   
	   return blnResult;
	} 	
//This function will check whether a input text box is having a valid number or not
//according to the business requirement negatives are considered as invalid Numbers
function IsNumeric(pInputValue){
   var strValidChars = "0123456789.";
   var strChar;
   var blnResult = true;
   var TxtBxVal=pInputValue;                
   var Flag=isNaN(TxtBxVal);
   if(Flag){
     blnResult = false;
   }else if(TxtBxVal.charAt(TxtBxVal.length-1)=="."){
     blnResult = false;
   }else{
	   for (var i = 0; i < TxtBxVal.length && blnResult == true; i++){
	      strChar = TxtBxVal.charAt(i);
	      if (strValidChars.indexOf(strChar) == -1){
	           blnResult = false;
	         }
	    }
   }   
   return blnResult;
}  
//This function will check whether a input text box is having a valid number or not
//according to the business requirement negatives are considered as invalid Numbers
function IsWholeNumber(pInputValue){
	var strValidChars = "0123456789";
	var strChar;
	var blnResult = true;
	var TxtBxVal=pInputValue;                
	var Flag=isNaN(TxtBxVal);
	if(Flag){
	 blnResult = false;
	}else{
		   for (var i = 0; i < TxtBxVal.length && blnResult == true; i++){
		      strChar = TxtBxVal.charAt(i);
		      if (strValidChars.indexOf(strChar) == -1){
		           blnResult = false;
		         }
		    }
	}   
	return blnResult;
}

	/*  ------WIDELY USED-----
	 *	pContainerHeader :div container for header 
	 *	pContainerData	 :div container for data
	 *	pCols			 :No of Columns
	 *	pRows			 :No of rows 
	 *	pCellWidth		 :width of each cells
	 *	pMatrixValue	 :Cell Value Matrix (2d arrya)
	 *	pLink			 :Hyper Link URL
	 *	
	 */
	
	function Matrix(pContainerHeader,pContainerData,pCols,pRows,pCellWidth,pCellAlign,pMatrixValue,pLink,pMatrixType)
	{	
		var jContainerHeader=pContainerHeader;
		var jContainerData=pContainerData;
		var jCols=pCols;
		var jRows=pRows;
		var jCellWidth=pCellWidth;
		var jCellAlign=pCellAlign;
		var jMatrixValue=pMatrixValue;
		var jLink="";
		var jMatrixType=pMatrixType;
		var jParam;			
		if(jMatrixType=='LiveLink'){
			jLink=pLink;
		}else if(jMatrixType=='DeadLink'){
		    jLink="#";
		}
		//header preparation
		var root=document.getElementById(jContainerHeader);
		var tab=document.createElement('table');
		tab.className="mytable";
		var tbo=document.createElement('tbody');
		var row, cell;
		row=document.createElement('tr');
		cell=document.createElement('th');
		cell.style.backgroundColor = "#99CCFF";	
		for(var j=0;j<jCols;j++){
			cell=document.createElement('th');
			cell.style.backgroundColor = "#99CCFF";	
			cell.style.width=jCellWidth[j];	
			//cell.style.textAlign=jCellAlign[j];
			cell.appendChild(document.createTextNode(jMatrixValue[0][j]));			
			row.appendChild(cell);
				
		}
		tbo.appendChild(row);
		tab.appendChild(tbo);
		root.appendChild(tab);
		//data preparation
		var root=document.getElementById(jContainerData);
		var tab=document.createElement('table');
		tab.className="mytable";
		var tbo=document.createElement('tbody');
		for(var i=1;i<jRows;i++)
		{
			row=document.createElement('tr');
			if (i%2==0){
				row.style.backgroundColor = "#E0EBEB";		 
			}else{
				row.style.backgroundColor = "#ffffff";
			}
			for(var j=0;j<jCols;j++){
			    if(j==0){
			    	cell=document.createElement('td');
			    	cell.style.width = jCellWidth[j];
			    	cell.style.textAlign=jCellAlign[j];
			    	cell.style="white-space: nowrap";
			    	jParam=jLink+pMatrixValue[i][j];
			    	var a = document.createElement('a');
			    	var linkText = document.createTextNode(jMatrixValue[i][j]);
					a.appendChild(linkText);
					a.href =jParam;
					cell.appendChild(a);
					row.appendChild(cell);
			    }else {
			    	cell=document.createElement('td');	
			    	cell.style.width = jCellWidth[j];
			    	cell.style.textAlign=jCellAlign[j];	
			    	cell.style="white-space: nowrap";
			    	cell.appendChild(document.createTextNode(jMatrixValue[i][j]));
					row.appendChild(cell);
			    }				
			}
			tbo.appendChild(row);
		}
		tab.appendChild(tbo);
		root.appendChild(tab);
	}
      
	/*  
	 *  this function does not provide any hyper link
	 *  this function gives header only no summary rows
	 *  
	 *	pContainerHeader :div container for header 
	 *	pContainerData	 :div container for data
	 *	pCols			 :No of Columns
	 *	pRows			 :No of rows 
	 *	pCellWidth		 :width of each cells
	 *	pMatrixValue	 :Cell Value Matrix (2d arrya)
	 *	---Not in Use
	 */
	
	function MatrixReport(pContainerHeader,pContainerData,pCols,pRows,pCellWidth,pCellAlign,pMatrixValue)
	{	
		var jContainerHeader=pContainerHeader;
		var jContainerData=pContainerData;
		var jCols=pCols;
		var jRows=pRows;
		var jCellWidth=pCellWidth;
		var jCellAlign=pCellAlign;
		var jMatrixValue=pMatrixValue;
		
		//header preparation
		var root=document.getElementById(jContainerHeader);
		var tab=document.createElement('table');
		tab.className="mytable";
		
		var tbo=document.createElement('tbody');
		var row, cell;
		row=document.createElement('tr');
		cell=document.createElement('th');
		cell.style.backgroundColor = "#800000";	
		
		for(var j=0;j<jCols;j++){
			cell=document.createElement('th');
			cell.style.backgroundColor = "#800000";	
			cell.style.width=jCellWidth[j];	
			cell.align=jCellAlign[j];
			cell.style="white-space: nowrap";
			cell.appendChild(document.createTextNode(jMatrixValue[0][j]));		
			cell.style.color="#ffffff";
			cell.style.fontSize="15px";
			cell.style.fontWeight="bold";
			cell.style.fontFamily="sans-serif, Arial";		
			row.appendChild(cell);		
		}
		tbo.appendChild(row);
		tab.appendChild(tbo);
		root.appendChild(tab);
		//data preparation
		var root=document.getElementById(jContainerData);
		var tab=document.createElement('table');
		tab.className="mytable";
		var tbo=document.createElement('tbody');
		for(var i=1;i<jRows;i++)
		{		
			row=document.createElement('tr');		
			if (i%2==0){
				row.style.backgroundColor = "#F4FAFF";
			}else{
				row.style.backgroundColor = "#ECF6FF";
			}
			for(var j=0;j<jCols;j++){
			   
			    	cell=document.createElement('td');	
			    	cell.style.width = jCellWidth[j];
			    	cell.align=jCellAlign[j];	
			    	cell.style="white-space: nowrap";
			    	cell.appendChild(document.createTextNode(jMatrixValue[i][j]));
			    	cell.style.fontSize="14.5px";
			    	cell.style.fontFamily="sans-serif, Arial";
					row.appendChild(cell);							
			}
			
			tbo.appendChild(row);
		}
		tab.appendChild(tbo);
		root.appendChild(tab);
	}
	  	
	/*  
	 *  this function does not provide any hyper link
	 *  this function gives header summary rows both
	 *	pContainerHeader :div container for header 
	 *	pContainerData	 :div container for data
	 *	pCols			 :No of Columns
	 *	pRows			 :No of rows 
	 *	pCellWidth		 :width of each cells
	 *	pMatrixValue	 :Cell Value Matrix (2d arrya)
	 *	--not in use
	 */
		
function MatrixReportSummary(pContainerHeader,pContainerData,pContainerSummary,pCols,pRows,pCellWidth,pCellAlign,pMatrixValue)
{	
	var jContainerHeader=pContainerHeader;
	var jContainerData=pContainerData;
	var jContainerSummary=pContainerSummary;
	var jCols=pCols;
	var jRows=pRows;
	var jCellWidth=pCellWidth;
	var jCellAlign=pCellAlign;
	var jMatrixValue=pMatrixValue;
	
	//header preparation
	var root=document.getElementById(jContainerHeader);
	var tab=document.createElement('table');
	tab.className="mytable";
	var tbo=document.createElement('tbody');
	var row, cell;
	row=document.createElement('tr');
	cell=document.createElement('th');
	cell.style.backgroundColor = "#800000";	
	for(var j=0;j<jCols;j++){
		cell=document.createElement('th');
		cell.style.backgroundColor = "#800000";	
		cell.style.width=jCellWidth[j];	
		cell.style.textAlign=jCellAlign[j];
		cell.style="white-space: nowrap";
		cell.appendChild(document.createTextNode(jMatrixValue[0][j]));
		cell.style.color="#ffffff";
		cell.style.fontSize="15px";
		cell.style.fontWeight="bold";
		cell.style.fontFamily="sans-serif, Arial";
		row.appendChild(cell);
	}
	tbo.appendChild(row);
	tab.appendChild(tbo);
	root.appendChild(tab);
	//data preparation
	var root=document.getElementById(jContainerData);
	var tab=document.createElement('table');
	tab.className="mytable";
	var tbo=document.createElement('tbody');
	for(var i=1;i<jRows;i++)
	{
		row=document.createElement('tr');
		if (i%2==0){
			row.style.backgroundColor = "#F4FAFF";
		}else{
			row.style.backgroundColor = "#ECF6FF";
		}
		for(var j=0;j<jCols;j++){
		   
		    	cell=document.createElement('td');	
		    	cell.style.width = jCellWidth[j];
		    	cell.style.textAlign=jCellAlign[j];	
		    	cell.style="white-space: nowrap";
		    	cell.appendChild(document.createTextNode(jMatrixValue[i][j]));
		    	cell.style.fontSize="14.5px";
		    	cell.style.fontFamily="sans-serif, Arial";
				row.appendChild(cell);
		}
		
		tbo.appendChild(row);
	}
	tab.appendChild(tbo);
	root.appendChild(tab);
	//summary preparation
	var root=document.getElementById(jContainerSummary);
	var tab=document.createElement('table');
	tab.className="mytable";
	var tbo=document.createElement('tbody');
	var row, cell;
	row=document.createElement('tr');
	cell=document.createElement('th');
	//cell.style.backgroundColor = "#800000";	
	for(var j=0;j<jCols;j++){
		cell=document.createElement('th');
		cell.style.backgroundColor = "#BDB76B";	
		cell.style.width=jCellWidth[j];	
		//cell.style.textAlign=jCellAlign[j];
		cell.style="white-space: nowrap";
		cell.appendChild(document.createTextNode(jMatrixValue[jRows-1][j]));
		cell.style.color="#000000";
		cell.style.fontSize="15px";
		cell.style.fontWeight="bold";
		cell.style.fontFamily="sans-serif, Arial";
		row.appendChild(cell);		
	}
	tbo.appendChild(row);
	tab.appendChild(tbo);
	root.appendChild(tab);
}
  
	/*  this not in use now this uses a jquery :
	*	DtPicker.js and  this will work only with this date picker js
	*	how to use this function onclick="ShowCal(this)"
    */
    function ShowCal(pDateHolderObj){             
           NewCal(document.getElementById(pDateHolderObj.id).id,'DDMMMYYYY');
    }
    
    function ResetForm(pFormId){
    	document.getElementById(pFormId).reset();
    }
    
    /* disable all div elements */
    function DivDisable(pDivName){
        document.getElementById(pDivName).disabled =true;
        var nodes = document.getElementById(pDivName).getElementsByTagName('*');
        for(var i = 0; i < nodes.length; i++){
        	nodes[i].disabled = true;
        }
    }
    /* enable all div elements */
    function DivEnable(pDivName){
        document.getElementById(pDivName).disabled =false;
        var nodes = document.getElementById(pDivName).getElementsByTagName('*');
        for(var i = 0; i < nodes.length; i++){
        	nodes[i].disabled = false;
        }
    }
    
    /* to display div 
     * pDiv : name of the div to display
     * 
     * */
    function DivVisible(pDiv) {
        var dlg = document.getElementById(pDiv);
        dlg.style.display = "block";        
    }
    
    /* to display div 
     * pDiv : name of the div to display
     * 
     * */
    function DivInVisible(pDiv) {
        var dlg = document.getElementById(pDiv);
        dlg.style.display = "none";        
    }
    
    /* only html content will be printed*/
    function DivPrint(divName) {
        var printContents = document.getElementById(divName).innerHTML;
        var originalContents = document.body.innerHTML;
        document.body.innerHTML = printContents;
        window.print();
        document.body.innerHTML = originalContents;
   }
	
    function CheckSession() {   
    	var jFlag=false;
    	$.ajax({  
          type: "GET",  
          url: "CommonCheckSession.do", 
          dataType:"json", 
          cache:false,
          async:false,
          //data: "exploreKey=" + pRefKey,  
          //data: { "exploreKey":TmpStr, "userId":"R249766" },   //how to populate form bean
          success: function(response){   
             		//var Records=0;
          		$.each(response, function(i, employeeId){               
             			Records=parseInt(i)+1;
          		});
		            if (response[0]==='Session Expired'){
		            	//alert("Invalid Session! \n Close Browser & Login Again !");	
		                SubmitForm('SessionExpire.do');	
		                jFlag=false;
		            } else { 
		              //alert(response[0]);	
		              jFlag=true;			                                                      
		           }           
		          },  
	        error: function(e){  
	               alert('AJAX Error Occured:' + e);
			       SubmitForm('Error.do');			       
	               
	        }  
    	}); 
           
    	 return jFlag; 
	}   
    
    /* to display popup used in report for taking parameter 
     * cover : name of the div to cover the screen
     * 
     * */
    function PopUpShow(pDiv) {
        var cvr = document.getElementById("cover");
        var dlg = document.getElementById(pDiv);
        cvr.style.display = "block";
        dlg.style.display = "block";
        if (document.body.style.overflow = "hidden") {
        	cvr.style.width = "100%";
            cvr.style.height = "100%";
        }
    }
    function PopUpClose(pDiv) {
        var cvr = document.getElementById("cover");
        var dlg = document.getElementById(pDiv);
        cvr.style.display = "none";
        dlg.style.display = "none";
        document.body.style.overflowY = "";
    }
    
    /*
     * Auto close popup
     * pDiv	: id of the div to auto close
     * 
     */
    function PopUpAutoClose(pDiv){
    	 $("#"+pDiv).dialog({
             height: 140,
              modal: false,
              open: function(event, ui){
                 setTimeout("$('#"+pDiv+"').dialog('close')",2500);
              },
              show: {effect: "fade",duration: 700},
              hide: {effect: "fade",duration: 1500},          
          });
    }
    
    
    /* 
     * this function enable/disable the exchange rate box
     * ****************************************
     * pCcy	: Currency Display select box id
     * pExRt: Exchange Rate Entry text box id
     * ***************************************
     * */
    function ExchangeRateDisplay(pHomeCcy,pCcy,pExRt){
    	var jCcy=document.getElementById(pCcy).options[document.getElementById(pCcy).selectedIndex].value;
    	if(jCcy==pHomeCcy){
    		document.getElementById(pExRt).value='1.00000';
    		//$("#"+pExRt).removeClass("textbox");
    		$("#"+pExRt).addClass("readonly");	
    		$("#"+pExRt).attr("disabled",true);
    	}else{
    		$("#"+pExRt).val(parseFloat($("#"+pExRt).val()).toFixed(5)); 
    		$("#"+pExRt).removeClass("readonly");
    		$("#"+pExRt).addClass("textbox");
    		$("#"+pExRt).attr("disabled",false);
    		
    	}
    }
    /* 
     * This function calculate home amount and finally display then in proper format
     * ***********************************************
     * pAmt				:Actual Amount text box id
     * pExRt			:Exchange Rate 
     * pAmtHome			:Home Amount Id
     * pHomeCcy			:Home currency value; INR,BDT,USD..
     * pShowComma		:location(span) id to display comma separated home amount
     * pShowAmtInWords	:span to display amount in words
     * pShowHomeCcy		:span to display home currency
     * **************************************************
     * 
     * */
    function CalHomeAmount(pAmt,pExRt,pAmtHome,pHomeCcy,pShowComma,pShowAmtInWords,pShowHomeCcy){	
    	var jAmt=$("#"+pAmt).val();
    	var jRate=$("#"+pExRt).val();
    	if(jAmt.length>0 && jRate.length>0){
    		$("#"+pAmtHome).val(parseFloat(jAmt*jRate).toFixed(2));
    		var jAmountHome=$("#"+pAmtHome).val();
    		if(AmountValidateMaxLength(jAmountHome)==true){
    			alert("Amount Limit Exceeded (max 14 digit allowed) !");			
    		}else{			
    		}
    		DisplayAmountHome(pShowComma,pShowAmtInWords,pShowHomeCcy,jAmountHome,pHomeCcy);		  	 	
    	}
    } 
    
    /*
     * 
     * this function creates the hidden elements at a given location inside the html doc
     * pFormLoc	:loaction of the hidden elements
     * pId		: id of the hidden element
     * pName	: name of the hidden elements
     * pValue	: values assign in the hidden elements
     * if only name is assigned then elements will form an array
     * */
    function CreateHiddenElement(pFormLoc,pId,pName,pValue){
    	 var elementHidden=document.createElement('input');
         var formHidden = document.getElementById(pFormLoc);
         elementHidden.type = 'hidden';
         elementHidden.name = pId;
         elementHidden.name = pName;
         elementHidden.value = pValue;
         formHidden.appendChild(elementHidden);
             
    }
    
    function RoundNumber(pObj){
    	var jNumber=$(pObj).val();
    	if(jNumber.length>0){
    		$(pObj).val(parseFloat($(pObj).val()).toFixed(2));        	
    	}else{
    		$(pObj).val("");
    	}
    	
    }
    
    function RoundExchangeRate(pObj){
    	var jRate=$(pObj).val();
    	if(jRate.length>0){
    		$(pObj).val(parseFloat($(pObj).val()).toFixed(5));
        	jRate=$(pObj).val();
        	if(jRate.length>9){
        	  alert("Exchange rate exceeded maximum limit ! \n (max intergers=3, max decimals=5)");
        	  $(pObj).val("");      	
        	}       	
    	}else{
    		$(pObj).val("");
    	}
    	
    	    	
    }
    
    function CheckSearchBox(pObj){
    	if(pObj.value==""){
    		   pObj.value="ALL";	
		}else if(pObj.value=="ALL"){
			pObj.value="";
		}
    }
    
  