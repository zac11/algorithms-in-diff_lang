let s = 'i am checking this string to see how many times each character appears';
[...s].reduce((a, e) => { 
    a[e] = a[e] ? a[e] + 1 : 1; console.log(a) },
     {}); 