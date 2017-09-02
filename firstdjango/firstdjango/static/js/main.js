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
	group = searchParams.get("Group")
	if (group == 'Student'){
		document.getElementById('college-checkbox').checked = true;
		document.getElementById('library-checkbox').checked = true;
		document.getElementById('colleges-list').style.display = 'inline-block';
		document.getElementById('libraries-list').style.display = 'inline-block';
	}
	
	if (group == 'Tourist'){
		document.getElementById('hotel-checkbox').checked = true;
		document.getElementById('library-checkbox').checked = true;
		document.getElementById('hotels-list').style.display = 'inline-block';
		document.getElementById('libraries-list').style.display = 'inline-block';
	}
	
	if (group == 'BusinessMan'){
		document.getElementById('hotel-checkbox').checked = true;
		document.getElementById('industry-checkbox').checked = true;
		document.getElementById('hotels-list').style.display = 'inline-block';
		document.getElementById('industries-list').style.display = 'inline-block';
	}
}

function rowLink(address){
	window.location = address;
}
