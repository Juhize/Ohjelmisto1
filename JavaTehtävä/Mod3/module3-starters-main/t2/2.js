'use strict';

const targetElem = document.querySelector('#target');

targetElem.classList.add('my-list')

targetElem.innerHTML =`
<li>First item</li>
<li class = my-item>Second item</li>
<li>Third item</li>
`;