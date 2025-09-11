// Handling dynamic Input Field Height w.r.t content:  
import {useRef} from 'react';
const handleInput = () => {
 const mainRef = useRef(mainDivRef);
}


<div ref={mainDivRef}>
 <textarea 
  ref={textareaRef}
   placeholder={"ask me anything!"}
   value={value}
   onInput={handleInput}
   onChange={(e) => handleChange(e.target.value)}
   />
   

</div>
