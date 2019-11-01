var body = document.body, 
    r = document.querySelector('#r'),
    g = document.querySelector('#g'),
    b = document.querySelector('#b'),
    l = document.querySelector('#l'),
    r_out = document.querySelector('#r_out'),
    g_out = document.querySelector('#g_out'),
    b_out = document.querySelector('#b_out'),
    hex_out = document.querySelector('#hex');

function setColor(){

  r_out.value = parseInt(((r.value * l.value) / 255), 10);
  g_out.value = parseInt(((g.value * l.value) / 255), 10);
  b_out.value = parseInt(((b.value * l.value) / 255), 10);

  var r_hex = parseInt(r_out.value, 10).toString(16),
      g_hex = parseInt(g_out.value, 10).toString(16),
      b_hex = parseInt(b_out.value, 10).toString(16),
      hex = "#" + pad(r_hex) + pad(g_hex) + pad(b_hex);
  body.style.backgroundColor = hex; 
  hex_out.value = hex;
}

function pad(n){
  return (n.length<2) ? "0"+n : n;
}

l.addEventListener('change', function(){
  l_out.value = l.value
  setColor();
})

r.addEventListener('change', function() {
  setColor();
}, false);

r.addEventListener('input', function() {
  setColor();
}, false);

g.addEventListener('change', function() {
  setColor();
}, false);

g.addEventListener('input', function() {
  setColor();
}, false);

b.addEventListener('change', function() {
  setColor();
}, false);

b.addEventListener('input', function() {
  setColor();
}, false);