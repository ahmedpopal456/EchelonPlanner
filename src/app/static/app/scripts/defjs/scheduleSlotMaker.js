function generateSlots(x) {

	var currSlots = document.getElementById("classSlots");

    removeChildren(currSlots);

    for(i=0; i < x; i++){
        var inputA = document.createElement('input');
        inputA.id = "CourseID";
        inputA.type = "text";
        inputA.placeholder = "CourseID";
        var inputB = document.createElement('input');
        inputB.id = "Lecture Section";
        inputB.type = "text";
        inputB.placeholder = "Lecture Section";
        var inputC = document.createElement('input');
        inputC.id = "Tutorial Section";
        inputC.type = "text";
        inputC.placeholder = "Tutorial Section";
        var inputD = document.createElement('input');
        inputD.id = "Lab Section";
        inputD.type = "text";
        inputD.placeholder = "Lab Section";

        currSlots.appendChild(inputA);
        currSlots.appendChild(inputB);
        currSlots.appendChild(inputC);
        currSlots.appendChild(inputD);
    }

}