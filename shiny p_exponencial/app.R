
library(shiny)
library(ggplot2)
rsconnect::setAccountInfo(name='branly-ratamanche2',
                          token='D286EC165B33BF4A1599A4A550584713',
                          secret='wTG4evi/L/8xCXgn+o3uEQvtDp3v6kk0GjwZCUzO')
ui <- fluidPage(
  titlePanel("Calculadora de Distribución Exponencial"),
  sidebarLayout(
    sidebarPanel(
      sliderInput("rate",
                  "Tasa (\u03BB):",
                  min = 0.1,
                  max = 5,
                  value = 1,
                  step = 0.1),
      numericInput("x_value",
                   "Valor de x:",
                   min = 0,
                   value = 1,
                   step = 0.1),
      actionButton("calc", "Calcular Probabilidad")
    ),
    mainPanel(
      plotOutput("densityPlot"),
      textOutput("probDensity"),
      plotOutput("distributionPlot"),
      textOutput("probCumulative")
    )
  )
)

server <- function(input, output) {
  output$densityPlot <- renderPlot({
    x <- seq(0, 10, length.out = 1000)
    y <- dexp(x, rate = input$rate)
    selected_y <- dexp(input$x_value, rate = input$rate)
    
    ggplot(data.frame(x, y), aes(x, y)) +
      geom_line(color = "purple") +
      geom_vline(xintercept = input$x_value, linetype = "dashed", color = "red") +
      geom_point(aes(x = input$x_value, y = selected_y), color = "red", size = 3) +
      labs(title = "Función de Densidad de Probabilidad Exponencial",
           x = "x",
           y = "Densidad")
  })
  
  output$probDensity <- renderText({
    selected_y <- dexp(input$x_value, rate = input$rate)
    paste("Densidad de probabilidad en x =", input$x_value, "es", round(selected_y, 4))
  })
  
  output$distributionPlot <- renderPlot({
    x <- seq(0, 10, length.out = 1000)
    y <- pexp(x, rate = input$rate)
    selected_y <- pexp(input$x_value, rate = input$rate)
    
    ggplot(data.frame(x, y), aes(x, y)) +
      geom_line(color = "orange") +
      geom_vline(xintercept = input$x_value, linetype = "dashed", color = "red") +
      geom_point(aes(x = input$x_value, y = selected_y), color = "red", size = 3) +
      labs(title = "Función de Distribución Acumulativa Exponencial",
           x = "x",
           y = "Probabilidad Acumulada")
  })
  
  output$probCumulative <- renderText({
    selected_y <- pexp(input$x_value, rate = input$rate)
    paste("Probabilidad acumulada para x =", input$x_value, "es", round(selected_y, 4))
  })
}

shinyApp(ui = ui, server = server)
