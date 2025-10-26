def main():
    with open('input.txt') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    topic = lines[0]
    project_id = lines[1]
    protocols = lines[2:4]
    metrics = lines[4]
    scenario = lines[5]

    report = []
    report.append(f"Topic: {topic}")
    report.append(f"Project ID: {project_id}")
    report.append(f"Protocols Compared: {', '.join(protocols)}")
    report.append(metrics)
    report.append(scenario)
    report.append('\nResults/Comments:')
    report.append('- TCP offers reliable transmission but increases latency, which may impact real-time video negatively.')
    report.append('- UDP provides minimal latency, ideal for live streaming, but can experience packet loss.')
    report.append('- For on-demand video, TCP’s reliability is beneficial; for real-time, UDP is usually preferred.')

    with open('output.txt', 'w') as out:
        for line in report:
            print(line)         # Shows in workflow logs
            out.write(line + '\n')  # Saves to artifact

if __name__ == "__main__":
    main()
