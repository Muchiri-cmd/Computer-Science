Public Class Form1

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim i As Integer = 1
        Dim MaraNgapi As Integer
        Dim Jina As String

        Jina = InputBox("Enter his/her name please")
        MaraNgapi = InputBox("How many times do you want message to display ")

        While (i <= MaraNgapi)
            MessageBox.Show(i & " " & Jina & " Go to the people,live among the people,love and serve the people")
            i = i + 1
        End While
        MessageBox.Show(Jina & " Twakupenda sana. WEWE ni WETU ")

        Do While (i <= MaraNgapi)
            MessageBox.Show("This is a do while loop ")
            i = i + 1
        Loop
        MessageBox.Show("All done")

        Do
            MessageBox.Show("Post condition do while ")
            i = i + 1
        Loop While (i <= MaraNgapi)

        Do Until (i > MaraNgapi)
            MessageBox.Show("do until pre condition ")
            i = i + 1
        Loop

        Do
            MessageBox.Show("do until post condition ")
            i = i + 1
        Loop
    End Sub
End Class
