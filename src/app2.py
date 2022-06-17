def powers_of_two():
    result = "<table>"
    result += "<tr> <th>N</th> <th>2<sup>N</sup></th></tr>"
    for i in range(20):
        result += f"<tr> <td> {i} </td> <td> {2**i} </td> </tr>"

    result += "</table>"
    return result
