Principio S (Princípio da responsabilidade única) & O (Princípio Aberto-Fechado)

Para ilustrar esses princípios, criei um exemplo em Python, no qual a classe 'Shape' representa diversas formas geométricas e faz o calculo da área de diferentes formas, como círculos e retângulos.

Código que viola esses princípios:

![image](https://github.com/MagalhaesExe/Principio_SOLID/assets/125324885/5e9c15dd-5783-47eb-8604-e8acde45d71f)

A classe 'Shape' é responsável por determinar o tipo da forma e calcular sua área, violando o SRP. Além disso, ao adicionar uma nova forma geométrica, como um triângulo, precisamos modificar diretamente a classe Shape, violando o OCP.
Este código pode funcionar para os tipos de forma existentes, mas torna-se rapidamente insustentável à medida que adicionamos mais tipos de formas.

Código que segue os princípios:

![image](https://github.com/MagalhaesExe/Principio_SOLID/assets/125324885/31b18bcc-3175-48e0-9501-4e6a33af797f)

O SRP é seguido corretamente, pois a classe 'Shape' tem apenas uma responsabilidade: definir o comportamento comum para todas as formas geométricas. As classes 'Circle' e 'Rectangle' têm a responsabilidade de calcular suas próprias áreas.
Já o OCP é observado na função calculate_total_area(). Pode ser adicionado novas formas geométricas, como um quadrado ou um triângulo, estendendo o comportamento da função calculate_total_area() sem precisar modificar seu código fonte original.


Principio I (Princípio da substituição de Liskov) & Prefira Composição a Herança

