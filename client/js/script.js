        // setup the base API URL to call.
        // We'll add to this to make the various different API calls
const apiurl = 'http://localhost:5000';

        // Grab the output HTML element
const output = document.getElementById('output');

        // addResult simply takes an "item" JSON object
        // creates a table row "tr" for that item element
        // and adds it to the output element
function addResult(item) {
        // if it's an object, just add the items to the output html.
    const result = document.createElement('tr');
        // NOTE: id's are prefixed with "pn_" just so it has a bit more context when reading them.
        // result.id = `pn_${item.part_number}`;
        // result.textContent = `${item.distributor} sells a ${item.brand} ${item.speed} speed ${item.ratio} for £${item.rrp}`;
        // output.appendChild(result);
        // this is outdated code that may come in handy in the future
    const resultBr = document.createElement('td');
        // this is creating the table data, living within the table row "tr"
    resultBr.textContent = `${item.brand}`;
        // showing the brand data from the database
    result.appendChild(resultBr);
         // adding the data to the row

    const resultCM = document.createElement('td');
    resultCM.textContent = `${item.model}`; // `` is used to define a string element, ${} is used for grabing js information
    result.appendChild(resultCM);

    const resultSpeed = document.createElement('td');
    resultSpeed.textContent = `${item.speed}`;
    result.appendChild(resultSpeed);

    const resultRatio = document.createElement('td');
    resultRatio.textContent = `${item.ratio}`;
    result.appendChild(resultRatio);

    const resultPN = document.createElement('td');
    resultPN.textContent = `${item.part_number}`;
    result.appendChild(resultPN);

    const resultPrice = document.createElement('td');
    resultPrice.textContent = `£${item.rrp}`; 
    result.appendChild(resultPrice);

    const resultDistro = document.createElement('td');
    resultDistro.textContent = `${item.distributor}`;
    result.appendChild(resultDistro);

    const resultLink = document.createElement('td');
    const link = document.createElement('a')
    link.href = item.link 
    link.textContent = item.distributor;
    link.target = "_blank"; // this line opens the link in a new window
    resultLink.appendChild(link);
    result.appendChild(resultLink);

    output.appendChild(result);
        // adding the row to the table in the html file
}

        // This event listener captures the "submit" event that happens when you submit a form
        // You'll notice, we just grab the form by the tag selector, instead of by ID. 
        // This is because there's only one form on the page.
        // WARNING: This event will _also_ fire if another form on this page is submitted as well.
const form = document.querySelector('form').addEventListener('submit', (evt) => {
        // prevent the default form action taking place
        // This stops the page re-loading
        
    evt.preventDefault();

        // fetch the selections from the Form data we submitted
    const data = Object.fromEntries(new FormData(evt.target).entries());

        // clear the results on each submit
    output.innerHTML = '';

        // build the url we're going to call depending on selections
    let url = apiurl;

        // make sure the fields we're checking for do actually exist
    if (data.speed !== undefined) {
        if (data.speed != "Any") { 
            // add the speed path to the base api url if it's not "Any"
            // NOTE: the '+=' means "add this on to the end of the string"
            //
            // This will make the value of "url" "http://localhost:5000/speed/<speed>"
            url += `/speed/${data.speed}`;
        } else { 
            // if speed _is_ Any, change it to all for the api
            // This will make the value of "url" "http://localhost:5000/speed/all"
            url += "/speed/all"; 

        }
    }

    if (data.ratio !== undefined) {
        if (data.ratio != "Any") { 
            // add the ratio path to the url after speed if it's not "Any"
            // This will make the value of "url" "http://localhost:5000/speed/<speed>/ratio/<ratio>"
            url += `/ratio/${data.ratio}`; 
        } else {
            // if ratio _is_ Any, change it to all for the api
            // This will make the value of "url" "http://localhost:5000/speed/<speed>/ratio/all"
            url += "/ratio/all";
        }
    }

    if (data.brand !== undefined) {
        if (data.brand != "Any") {
            url += `/brand/${data.brand}`;
        } else {
            url += "/brand/all";
        }
    } 
        // same rules apply for this if statement as previous ratio and speed

    // Make the call to the API using the URL we've constructed above.
    fetch(url).then(response => {
            // Return early if we don't make a successful call to the API
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            // is all went well, translate the response into JSON
            return response.json();
        }).then(data => {
            // first, check if "data" actualy has anything in it
            if (data.length <= 0) {
                // If it doesn't, just say we didn't get any results and skip everything else.
                output.innerHTML = '<li>No results found</li>';
                return
            }
            // Because of how we build the API responses, the data will always be in an array.
            // So we can reliably call forEach.
            data.forEach(item => {
                // Next we need to check if each item in the data object is an array [] or an object {}.
                if (item.constructor == Array) {
                    item.forEach(itm => addResult(itm));
                }

                if (item.constructor == Object) { addResult(item); }
            });

        }).catch(error => {
            console.error('Error:', error);
            output.textContent = 'An error occurred while fetching data.';
        });
});

// const thead = document.getElementById("thead")

// function tableheader() {
//     var thead = document.getElementById("thead");
//   if (thead.style.display === "") {
//     thead.style.display = "none";
//   } else {
//     thead.style.display = "";
//   }
// }

// const submit_button = document.getElementById("submit_button")

// submit_button.addEventListener("click", tableheader());

// This function is incomplete

let scrollToTop = document.getElementById("scrollToTopBtn");
//  when button on html is clicked, the page jumps to the top
function scrollToTopBtn() {
    document.documentElement.scrollTop = 0;
}

// add to the code below to make the table header apear on command rather than 
// const theader = document.getElementById("theader");
// theader.classList.add('hidden');

function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("mytable");
    switching = true;
    //Set the sorting direction to ascending:
    dir = "asc"; 
    /*Make a loop that will continue until
    no switching has been done:*/
    while (switching) {
      //start by saying: no switching is done:
      switching = false;
      rows = table.rows;
      /*Loop through all table rows (except the
      first, which contains table headers):*/
      for (i = 1; i < (rows.length - 1); i++) {
        //start by saying there should be no switching:
        shouldSwitch = false;
        /*Get the two elements you want to compare,
        one from current row and one from the next:*/
        x = rows[i].getElementsByTagName("td")[n];
        y = rows[i + 1].getElementsByTagName("td")[n];
        /*check if the two rows should switch place,
        based on the direction, asc or desc:*/
        if (dir == "asc") {
          if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            //if so, mark as a switch and break the loop:
            shouldSwitch= true;
            break;
          }
        } else if (dir == "desc") {
          if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
            //if so, mark as a switch and break the loop:
            shouldSwitch = true;
            break;
          }
        }
      }
      if (shouldSwitch) {
        /*If a switch has been marked, make the switch
        and mark that a switch has been done:*/
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        //Each time a switch is done, increase this count by 1:
        switchcount ++;      
      } else {
        /*If no switching has been done AND the direction is "asc",
        set the direction to "desc" and run the while loop again.*/
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }