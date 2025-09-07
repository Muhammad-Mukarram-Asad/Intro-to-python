// hanlde search functionality in react:  

const [filteredList, setFilteredList] = useState([]);
const handleSearch = (e:React<HTMLDivElement>) => {
   const searchQuery = e.target.value.toLowerCase();
   if(searchQuery.trim() === "") 
     {
        setFilteredList([]);
        return;
     }
    else {
        const newFilteredlist = searchedList.filter((searchItem) => {
            searchItem.title.toLowercase().includes(searchQuery)
         });
        setFilteredList(newFilteredList);
    }
}
