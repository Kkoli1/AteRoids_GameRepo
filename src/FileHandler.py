from dataclasses import dataclass
from itertools import islice
from json import loads, dumps


@dataclass
class FileHandler:     
    fname:str = 'game'

    def update_content(self, json_obj:dict) -> None:
        """update game file contents 

        Args:
            json_obj (dict): dictionary that contains game information
        """        
        with open(self.fname + '.json', 'w') as f:
            f.write(dumps(json_obj, indent=4))
    
    def retrieve_content(self) -> dict: 
        """loads game file by parsing json object.

        Returns:
            dict: parsed json object as python dictionary.
        """        
        return loads(self.fname + '.json')


def sort_score(scores:dict, N:int = 10) -> dict: 
    """Sorts first N-elements of game scores

    Args:
        scores (dict): game score
        N (int, optional): Length of the new dictionary. Defaults to 10.

    Returns:
        dict: _description_
    """    
    ordered_dict =  {i:j for i,j in sorted(scores.items(), 
                    key = lambda x:x[1], reverse=True)}
    return {i:j for i,j in islice(ordered_dict.items(), N)}