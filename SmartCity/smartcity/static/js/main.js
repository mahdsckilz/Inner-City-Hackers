window.onload = initGroupCheckbox

function toggleList(element, modelClass){
	var modelList = document.getElementById(modelClass);
	try{
		if (element.checked == true){
			modelList.style.display = 'inline-block';
		}
		else {
			modelList.style.display = 'none';
		}
	}	
	catch(err){
		console.log("List Empty");
	}
}

function initGroupCheckbox(){
	var searchParams = new URLSearchParams(window.location.search);
	var checkBoxes = document.getElementsByClassName('poi-checkbox');

	for (var i = 0; i < checkBoxes.length; i++){
		checkBoxes[i].checked = false;
	}
	
	if (group == 'Student'){
		document.getElementById('college-checkbox').checked = true;
		document.getElementById('library-checkbox').checked = true;		
		document.getElementById('college-rows').style.display = 'inline-block';		
		document.getElementById('library-rows').style.display = 'inline-block';
	}
	
	if (group == 'Tourist'){
		document.getElementById('hotel-checkbox').checked = true;
		document.getElementById('library-checkbox').checked = true;
		document.getElementById('hotel-rows').style.display = 'inline-block';
		document.getElementById('library-rows').style.display = 'inline-block';
	}
	
	if (group == 'Business Person'){
		document.getElementById('hotel-checkbox').checked = true;
		document.getElementById('industry-checkbox').checked = true;
		document.getElementById('hotel-rows').style.display = 'inline-block';
		document.getElementById('industry-rows').style.display = 'inline-block';
	}
}

function rowLink(address){
	window.location = address;
}
