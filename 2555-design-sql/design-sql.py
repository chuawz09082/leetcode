class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        """
        Initializes the database with table names and column specifications.

        :param names: List of table names.
        :param columns: List containing the number of columns for each table.
        """
        self.names = names  # Store table names
        self.columns = columns  # Store column count for each table

        # Dictionary to track the next available row ID for each table.
        # Initialized with a list containing [1] as the first row ID.
        self.rowIds = collections.defaultdict(lambda: [1])

        # Dictionary to store table data as a dictionary of rowId -> row data.
        self.tables = collections.defaultdict(dict)

        

    def ins(self, name: str, row: List[str]) -> bool:
        """
        Inserts a row into the specified table.

        :param name: The name of the table.
        :param row: The list of column values representing the row.
        :return: True if the row is successfully inserted, False otherwise.
        """
        # Check if the table exists
        if name not in self.names:
            return False

        # Get the index of the table and validate column count
        idx = self.names.index(name)
        if len(row) != self.columns[idx]:
            return False  # Column count mismatch

        # Get the next available row ID
        rowId = self.rowIds[name][-1]
        
        # Append a new row ID for future insertions
        self.rowIds[name].append(rowId + 1)

        # Store the row in the table
        self.tables[name][rowId] = row

        return True  # Successful insertion

        

    def rmv(self, name: str, rowId: int) -> None:
        """
        Removes a row from the specified table by marking it as None.

        :param name: The name of the table.
        :param rowId: The row ID to remove.
        """
        # If the table doesn't exist or the rowId is not found, do nothing
        if name not in self.names or rowId not in self.tables[name]:
            return

        # Mark the row as None instead of deleting it to maintain row order
        self.tables[name][rowId] = None


    def sel(self, name: str, rowId: int, columnId: int) -> str:
        """
        Selects a specific column value from a row.

        :param name: The name of the table.
        :param rowId: The row ID.
        :param columnId: The 1-based column index.
        :return: The value at the specified column, or "<null>" if not found.
        """
        # Check if the table exists, rowId exists, row is not None, and columnId is within range
        if (
            name not in self.names or 
            rowId not in self.tables[name] or 
            self.tables[name][rowId] is None or 
            columnId > len(self.tables[name][rowId])
        ):
            return "<null>"

        # Return the value at the specified column (adjusting for 1-based indexing)
        return self.tables[name][rowId][columnId-1]

    def exp(self, name: str) -> List[str]:
        """
        Exports all non-deleted rows from a table in CSV-like format.

        :param name: The name of the table.
        :return: A list of strings, where each row is formatted as "rowId,value1,value2,...".
        """
        # If the table doesn't exist, return an empty list
        if name not in self.names:
            return []

        result = []
        memo = self.tables[name]  # Get the table data

        # Iterate over all rows in the table
        for key, value in memo.items():
            if value is not None:  # Skip deleted rows
                # Format the row as "rowId,value1,value2,..."
                current = str(key) + "," + ",".join(value)
                result.append(current)

        return result



# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)