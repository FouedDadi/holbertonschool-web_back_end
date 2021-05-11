export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (error) {
    queue.push(error.toSting());
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
