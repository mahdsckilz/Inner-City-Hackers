
function toggleList(element, $modelClass){
	var $modelList = document.getElementById($modelClass);
	console.log($modelClass);
	if (element.checked == true){
		$modelList.style.display = 'initial';
	}
	else {
		$modelList.style.display = 'none';
	}
}