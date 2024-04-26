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

O código utilizado é basicamente um sistema de gerenciamento de dispositivos eletrônicos em uma casa, como lâmpadas e televisões.

Código que viola esses príncipios:

![image](https://github.com/MagalhaesExe/Principio_SOLID/assets/125324885/48bc67e5-b552-4ac6-8b11-9f9e5395a748)

A classe 'TV' viola o Princípio da Segregação de Interfaces (ISP), pois ela tem métodos específicos para ligar e desligar uma lâmpada, que não são relevantes para uma TV em si. Além disso, em vez de usar composição para adicionar funcionalidades específicas, como o controle de uma lâmpada, a classe 'TV' inclui métodos diretamente relacionados à lâmpada, violando o princípio "Prefira Composição a Herança".

Código que segue os princípios:

![image](https://github.com/MagalhaesExe/Principio_SOLID/assets/125324885/36265b37-b364-420f-848a-f61a2aa02bd3)

Esse código é mais modular e organizado, pois define interfaces separadas para diferentes comportamentos, csda classe implementa apenas as interfaces relevantes para ela, mantendo o código coeso e focado em uma única responsabilidade e seguindo os princípios I e Prefira Composição a Herança. Além de resultar em um baixo acoplamento, facilitando a manutenção e extensão do código.
