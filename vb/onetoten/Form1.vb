Public Class Form1
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Dim index As Integer = 0

        While index <= 10
            Console.Write(index.ToString & " ")
            index += 1
        End While
        Console.WriteLine("")
        Console.ReadKey()

    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Dim index As Integer = 0
        Dim output As String
        While index <= 10
            output = output & index &
            vbNewLine
            index += 1
        End While
        MessageBox.Show(output)
    End Sub

    Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Button3.Click
        Dim a As Integer = 0
        Do While a <= 10
            Console.WriteLine("value of a: {0}", a)
            a = a + 1
        Loop
        Console.WriteLine("")
        Console.ReadKey()
    End Sub
End Class
