FROM quay.io/jupyter/minimal-notebook:afe30f0c9ad8

# Copy the Conda lock file
COPY conda-linux-64.lock /tmp/conda-linux-64.lock

# Create the 'term-deposit-predictor' environment
RUN mamba create --quiet --name term-deposit-predictor --file /tmp/conda-linux-64.lock \
    && mamba clean --all -y -f \
    && fix-permissions "${CONDA_DIR}" \
    && fix-permissions "/home/${NB_USER}"

# Install additional packages in the 'term-deposit-predictor' environment
RUN /opt/conda/envs/term-deposit-predictor/bin/pip install deepchecks==0.18.1

# Add the environment to Jupyter as a kernel
RUN /opt/conda/envs/term-deposit-predictor/bin/python -m ipykernel install --user --name term-deposit-predictor --display-name "Python (term-deposit-predictor)"

# Ensure permissions for the environment
RUN fix-permissions "/opt/conda/envs/term-deposit-predictor"

# Set environment variables
ENV CONDA_DEFAULT_ENV=term-deposit-predictor
ENV PATH="/opt/conda/envs/term-deposit-predictor/bin:$PATH"

# Override CMD to activate the environment and start Jupyter
CMD ["bash", "-c", "source /opt/conda/etc/profile.d/conda.sh && conda activate term-deposit-predictor && start-notebook.sh"]
