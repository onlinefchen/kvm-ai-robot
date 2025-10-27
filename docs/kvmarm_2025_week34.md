# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 12:03:50

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 292
- **总 Thread 数**: 24
- **大型 Thread** (>20封): 4 个

### 分类分布

- **PATCH**: 23 threads (273 邮件)
- **RFC**: 1 threads (19 邮件)

---

## 📌 PATCH

共 23 个 thread

---

### Thread 1: [PATCH v10 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 44 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 20 Aug 2025 15:55:20 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM（内核虚拟机）支持 Arm CCA（机密计算架构）的补丁系列（PATCH v10 00/43）。该系列补丁的主要目标是增强 KVM 在运行受保护虚拟机时的能力。

1. **原始补丁内容**：补丁系列主要添加了对 KVM 中运行受保护虚拟机的支持，涉及到 Arm CCA 的实现。补丁中修复了多个潜在问题，并更新了相关的能力和 ioctl 接口。

2. **历史讨论要点**：之前的讨论集中在如何处理虚拟机的内存管理、错误处理和与 RMM（Realm Management Monitor）之间的交互。特别是关于如何在虚拟机销毁时处理页表和内存的释放，以及如何在不同状态下管理虚拟机的运行。

3. **本周的新讨论与进展**：本周的讨论主要集中在补丁的具体实现上，包括：
   - 增强了对 MMIO（内存映射输入输出）操作的支持。
   - 允许 VMM（虚拟机监控器）在虚拟机创建前填充初始内容。
   - 处理虚拟机的 RIPAS（Realm IPA State）变化请求。
   - 提供了对 PMU（性能监控单元）的支持，确保在进入受保护虚拟机时正确管理 IRQ（中断请求）。
   - 更新了对 SVE（可扩展向量扩展）的支持，确保在 Realm 中正确配置最大向量长度。

整体而言，该系列补丁的实施将大幅提升 KVM 在处理 Arm CCA 的能力，确保虚拟机在安全和性能上的需求得到满足。

#### 📝 邮件列表

1. **[08-20 15:55]** [PATCH v10 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[08-20 15:55]** [PATCH v10 01/43] kvm: arm64: Include kvm_emulate.h in kvm/arm_psci.h
   - 发件人: Steven Price <steven.price@arm.com>
3. **[08-20 15:55]** [PATCH v10 02/43] arm64: RME: Handle Granule Protection Faults (GPFs)
   - 发件人: Steven Price <steven.price@arm.com>
4. **[08-20 15:55]** [PATCH v10 03/43] arm64: RME: Add SMC definitions for calling the RMM
   - 发件人: Steven Price <steven.price@arm.com>
5. **[08-20 15:55]** [PATCH v10 04/43] arm64: RME: Add wrappers for RMI calls
   - 发件人: Steven Price <steven.price@arm.com>
6. **[08-20 15:55]** [PATCH v10 05/43] arm64: RME: Check for RME support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
7. **[08-20 15:55]** [PATCH v10 06/43] arm64: RME: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
8. **[08-20 15:55]** [PATCH v10 07/43] arm64: RME: ioctls to create and configure realms
   - 发件人: Steven Price <steven.price@arm.com>
9. **[08-20 15:55]** [PATCH v10 08/43] kvm: arm64: Don't expose debug capabilities for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
10. **[08-20 15:55]** [PATCH v10 09/43] KVM: arm64: Allow passing machine type in KVM creation
   - 发件人: Steven Price <steven.price@arm.com>
11. **[08-20 15:55]** [PATCH v10 10/43] arm64: RME: RTT tear down
   - 发件人: Steven Price <steven.price@arm.com>
12. **[08-20 15:55]** [PATCH v10 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
13. **[08-20 15:55]** [PATCH v10 12/43] KVM: arm64: vgic: Provide helper for number of list registers
   - 发件人: Steven Price <steven.price@arm.com>
14. **[08-20 15:55]** [PATCH v10 13/43] arm64: RME: Support for the VGIC in realms
   - 发件人: Steven Price <steven.price@arm.com>
15. **[08-20 15:55]** [PATCH v10 14/43] KVM: arm64: Support timers in realm RECs
   - 发件人: Steven Price <steven.price@arm.com>
16. **[08-20 15:55]** [PATCH v10 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
17. **[08-20 15:55]** [PATCH v10 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Steven Price <steven.price@arm.com>
18. **[08-20 15:55]** [PATCH v10 17/43] arm64: RME: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Steven Price <steven.price@arm.com>
19. **[08-20 15:55]** [PATCH v10 18/43] KVM: arm64: Handle realm MMIO emulation
   - 发件人: Steven Price <steven.price@arm.com>
20. **[08-20 15:55]** [PATCH v10 19/43] arm64: RME: Allow populating initial contents
   - 发件人: Steven Price <steven.price@arm.com>
21. **[08-20 15:55]** [PATCH v10 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
22. **[08-20 15:55]** [PATCH v10 21/43] KVM: arm64: Handle realm VCPU load
   - 发件人: Steven Price <steven.price@arm.com>
23. **[08-20 15:55]** [PATCH v10 22/43] KVM: arm64: Validate register access for a Realm VM
   - 发件人: Steven Price <steven.price@arm.com>
24. **[08-20 15:55]** [PATCH v10 23/43] KVM: arm64: Handle Realm PSCI requests
   - 发件人: Steven Price <steven.price@arm.com>
25. **[08-20 15:55]** [PATCH v10 24/43] KVM: arm64: WARN on injected undef exceptions
   - 发件人: Steven Price <steven.price@arm.com>
26. **[08-20 15:55]** [PATCH v10 25/43] arm64: Don't expose stolen time for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
27. **[08-20 15:55]** [PATCH v10 26/43] arm64: RME: allow userspace to inject aborts
   - 发件人: Steven Price <steven.price@arm.com>
28. **[08-20 15:55]** [PATCH v10 27/43] arm64: RME: support RSI_HOST_CALL
   - 发件人: Steven Price <steven.price@arm.com>
29. **[08-20 15:55]** [PATCH v10 28/43] arm64: RME: Allow checking SVE on VM instance
   - 发件人: Steven Price <steven.price@arm.com>
30. **[08-20 15:55]** [PATCH v10 29/43] arm64: RME: Always use 4k pages for realms
   - 发件人: Steven Price <steven.price@arm.com>
31. **[08-20 15:55]** [PATCH v10 30/43] arm64: RME: Prevent Device mappings for Realms
   - 发件人: Steven Price <steven.price@arm.com>
32. **[08-20 15:55]** [PATCH v10 31/43] arm_pmu: Provide a mechanism for disabling the physical IRQ
   - 发件人: Steven Price <steven.price@arm.com>
33. **[08-20 15:55]** [PATCH v10 32/43] arm64: RME: Enable PMU support with a realm guest
   - 发件人: Steven Price <steven.price@arm.com>
34. **[08-20 15:55]** [PATCH v10 33/43] arm64: RME: Hide KVM_CAP_READONLY_MEM for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
35. **[08-20 15:55]** [PATCH v10 34/43] arm64: RME: Propagate number of breakpoints and watchpoints to userspace
   - 发件人: Steven Price <steven.price@arm.com>
36. **[08-20 15:55]** [PATCH v10 35/43] arm64: RME: Set breakpoint parameters through SET_ONE_REG
   - 发件人: Steven Price <steven.price@arm.com>
37. **[08-20 15:55]** [PATCH v10 36/43] arm64: RME: Initialize PMCR.N with number counter supported by RMM
   - 发件人: Steven Price <steven.price@arm.com>
38. **[08-20 15:55]** [PATCH v10 37/43] arm64: RME: Propagate max SVE vector length from RMM
   - 发件人: Steven Price <steven.price@arm.com>
39. **[08-20 15:55]** [PATCH v10 38/43] arm64: RME: Configure max SVE vector length for a Realm
   - 发件人: Steven Price <steven.price@arm.com>
40. **[08-20 15:55]** [PATCH v10 39/43] arm64: RME: Provide register list for unfinalized RME RECs
   - 发件人: Steven Price <steven.price@arm.com>
41. **[08-20 15:56]** [PATCH v10 40/43] arm64: RME: Provide accurate register list
   - 发件人: Steven Price <steven.price@arm.com>
42. **[08-20 15:56]** [PATCH v10 41/43] KVM: arm64: Expose support for private memory
   - 发件人: Steven Price <steven.price@arm.com>
43. **[08-20 15:56]** [PATCH v10 42/43] KVM: arm64: Expose KVM_ARM_VCPU_REC to user space
   - 发件人: Steven Price <steven.price@arm.com>
44. **[08-20 15:56]** [PATCH v10 43/43] KVM: arm64: Allow activating realms
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 2: [PATCH v7 00/29] KVM: arm64: Implement support for SME

**📧 邮件数**: 31 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 22 Aug 2025 02:53:29 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 ARM64 架构上实现对 SME（可扩展矩阵扩展）的支持的补丁系列（PATCH v7 00/29）。以下是讨论的主要内容：

1. **原始补丁内容**：该补丁系列的目标是为 KVM 实现对 SME 的支持，主要涉及新的向量长度配置、控制寄存器的访问，以及与 SVE（可扩展向量扩展）相关的状态管理。补丁中引入了新的系统寄存器，如 SMCR（SM 控制寄存器）和 SVCR（流模式控制寄存器），并定义了如何在用户空间访问这些寄存器。

2. **历史讨论要点**：之前的讨论集中在如何处理 SME 和 SVE 的向量长度配置，以及如何在 KVM 中实现对这些新寄存器的支持。补丁的设计考虑了与现有 SVE 功能的兼容性，确保在不同的虚拟机环境中能够正确管理寄存器状态。

3. **本周的新讨论与进展**：本周的讨论主要集中在补丁的具体实现细节上，包括对 SME 状态的上下文切换、异常处理、以及如何在嵌套虚拟机中支持 SME。补丁还扩展了自测功能，以确保新引入的寄存器能够被正确识别和访问。参与者 Mark Brown 提出了对 KVM ABI 的文档更新，确保开发者能够理解 SME 的使用和配置。

总的来说，本周的讨论进一步推动了 KVM 对 SME 的支持，确保了与 SVE 的兼容性，并为未来的开发奠定了基础。

#### 📝 邮件列表

1. **[08-22 02:53]** [PATCH v7 00/29] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[08-22 02:53]** [PATCH v7 01/29] arm64/sysreg: Update SMIDR_EL1 to DDI0601 2025-06
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[08-22 02:53]** [PATCH v7 02/29] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[08-22 02:53]** [PATCH v7 03/29] arm64/fpsimd: Decide to save ZT0 and streaming
 mode FFR at bind time
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[08-22 02:53]** [PATCH v7 04/29] arm64/fpsimd: Check enable bit for FA64 when
 saving EFI state
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[08-22 02:53]** [PATCH v7 05/29] arm64/fpsimd: Determine maximum virtualisable SME
 vector length
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[08-22 02:53]** [PATCH v7 06/29] KVM: arm64: Introduce non-UNDEF FGT control
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[08-22 02:53]** [PATCH v7 07/29] KVM: arm64: Pay attention to FFR parameter in SVE
 save and load
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[08-22 02:53]** [PATCH v7 08/29] KVM: arm64: Pull ctxt_has_ helpers to start of
 sysreg-sr.h
   - 发件人: Mark Brown <broonie@kernel.org>
10. **[08-22 02:53]** [PATCH v7 09/29] KVM: arm64: Move SVE state access macros after
 feature test macros
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[08-22 02:53]** [PATCH v7 10/29] KVM: arm64: Rename SVE finalization constants to
 be more general
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[08-22 02:53]** [PATCH v7 11/29] KVM: arm64: Document the KVM ABI for SME
   - 发件人: Mark Brown <broonie@kernel.org>
13. **[08-22 02:53]** [PATCH v7 12/29] KVM: arm64: Define internal features for SME
   - 发件人: Mark Brown <broonie@kernel.org>
14. **[08-22 02:53]** [PATCH v7 13/29] KVM: arm64: Rename sve_state_reg_region
   - 发件人: Mark Brown <broonie@kernel.org>
15. **[08-22 02:53]** [PATCH v7 14/29] KVM: arm64: Store vector lengths in an array
   - 发件人: Mark Brown <broonie@kernel.org>
16. **[08-22 02:53]** [PATCH v7 15/29] KVM: arm64: Implement SME vector length
 configuration
   - 发件人: Mark Brown <broonie@kernel.org>
17. **[08-22 02:53]** [PATCH v7 16/29] KVM: arm64: Support SME control registers
   - 发件人: Mark Brown <broonie@kernel.org>
18. **[08-22 02:53]** [PATCH v7 17/29] KVM: arm64: Support TPIDR2_EL0
   - 发件人: Mark Brown <broonie@kernel.org>
19. **[08-22 02:53]** [PATCH v7 18/29] KVM: arm64: Support SME identification registers
 for guests
   - 发件人: Mark Brown <broonie@kernel.org>
20. **[08-22 02:53]** [PATCH v7 19/29] KVM: arm64: Support SME priority registers
   - 发件人: Mark Brown <broonie@kernel.org>
21. **[08-22 02:53]** [PATCH v7 20/29] KVM: arm64: Provide assembly for SME register
 access
   - 发件人: Mark Brown <broonie@kernel.org>
22. **[08-22 02:53]** [PATCH v7 21/29] KVM: arm64: Support userspace access to streaming
 mode Z and P registers
   - 发件人: Mark Brown <broonie@kernel.org>
23. **[08-22 02:53]** [PATCH v7 22/29] KVM: arm64: Flush register state on writes to
 SVCR.SM and SVCR.ZA
   - 发件人: Mark Brown <broonie@kernel.org>
24. **[08-22 02:53]** [PATCH v7 23/29] KVM: arm64: Expose SME specific state to
 userspace
   - 发件人: Mark Brown <broonie@kernel.org>
25. **[08-22 02:53]** [PATCH v7 24/29] KVM: arm64: Context switch SME state for guests
   - 发件人: Mark Brown <broonie@kernel.org>
26. **[08-22 02:53]** [PATCH v7 25/29] KVM: arm64: Handle SME exceptions
   - 发件人: Mark Brown <broonie@kernel.org>
27. **[08-22 02:53]** [PATCH v7 26/29] KVM: arm64: Expose SME to nested guests
   - 发件人: Mark Brown <broonie@kernel.org>
28. **[08-22 02:53]** [PATCH v7 27/29] KVM: arm64: Provide interface for configuring and
 enabling SME for guests
   - 发件人: Mark Brown <broonie@kernel.org>
29. **[08-22 02:53]** [PATCH v7 28/29] KVM: arm64: selftests: Add SME system registers
 to get-reg-list
   - 发件人: Mark Brown <broonie@kernel.org>
30. **[08-22 02:53]** [PATCH v7 29/29] KVM: arm64: selftests: Add SME to set_id_regs
 test
   - 发件人: Mark Brown <broonie@kernel.org>
31. **[08-21 23:50]** Re: [PATCH v7 11/29] KVM: arm64: Document the KVM ABI for SME
   - 发件人: Randy Dunlap <rdunlap@infradead.org>

---

### Thread 3: [PATCH v4 00/28] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate)

**📧 邮件数**: 29 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 19 Aug 2025 21:51:28 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 的 ARM SMMUv3 驱动的多个补丁（PATCH v4 00/28），主要集中在实现嵌套翻译、命令队列（CMDQ）和流表（STE）的仿真等功能。

1. **原始补丁/问题的内容**：
   本系列补丁旨在为 KVM 提供 ARM SMMUv3 的支持，特别是通过 trap 和 emulate 实现嵌套翻译。补丁中包含了对 SMMU 驱动的重构和功能增强，以支持虚拟化环境中的 DMA 隔离。

2. **之前讨论要点**：
   之前的讨论主要集中在如何简化 SMMU 驱动的维护和实现嵌套翻译的复杂性。补丁版本的演变显示出从最初的完整 PV 接口实现到现在的基于 trap 和 emulate 的方法，反映了对维护性和性能的关注。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，补丁实现了多个关键功能，包括：
   - **命令队列的仿真**：通过对 CMDQ 的读写操作进行过滤和处理，确保命令的安全性和一致性。
   - **流表的仿真**：在接收到 CFGI_STE 命令时，更新 SMMU 的流表，确保虚拟化环境中的地址转换正确。
   - **GBPA 的仿真**：确保 GBPA 始终设置为 ABORT，防止主机绕过 SMMU。
   - **支持 io-pgtable**：为 SMMU 驱动添加了内存分配的钩子，以支持与 io-pgtable-arm 的集成。
   - **启用嵌套功能**：在 SMMU 控制命令队列和流表的情况下，允许嵌套翻译。

这些补丁的实施将增强 KVM 在 ARM 平台上的虚拟化能力，提供更好的设备隔离和内存管理。

#### 📝 邮件列表

1. **[08-19 21:51]** [PATCH v4 00/28] KVM: arm64: SMMUv3 driver for pKVM (trap and emulate)
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[08-19 21:51]** [PATCH v4 01/28] KVM: arm64: Add a new function to donate memory with prot
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[08-19 21:51]** [PATCH v4 02/28] KVM: arm64: Donate MMIO to the hypervisor
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[08-19 21:51]** [PATCH v4 03/28] KVM: arm64: pkvm: Add pkvm_time_get()
   - 发件人: Mostafa Saleh <smostafa@google.com>
5. **[08-19 21:51]** [PATCH v4 04/28] iommu/io-pgtable-arm: Move selftests to a separate file
   - 发件人: Mostafa Saleh <smostafa@google.com>
6. **[08-19 21:51]** [PATCH v4 05/28] iommu/io-pgtable-arm: Factor kernel specific code out
   - 发件人: Mostafa Saleh <smostafa@google.com>
7. **[08-19 21:51]** [PATCH v4 06/28] iommu/arm-smmu-v3: Split code with hyp
   - 发件人: Mostafa Saleh <smostafa@google.com>
8. **[08-19 21:51]** [PATCH v4 07/28] iommu/arm-smmu-v3: Move TLB range invalidation into
 a macro
   - 发件人: Mostafa Saleh <smostafa@google.com>
9. **[08-19 21:51]** [PATCH v4 08/28] iommu/arm-smmu-v3: Move IDR parsing to common functions
   - 发件人: Mostafa Saleh <smostafa@google.com>
10. **[08-19 21:51]** [PATCH v4 09/28] KVM: arm64: iommu: Introduce IOMMU driver infrastructure
   - 发件人: Mostafa Saleh <smostafa@google.com>
11. **[08-19 21:51]** [PATCH v4 10/28] KVM: arm64: iommu: Shadow host stage-2 page table
   - 发件人: Mostafa Saleh <smostafa@google.com>
12. **[08-19 21:51]** [PATCH v4 11/28] KVM: arm64: iommu: Add memory pool
   - 发件人: Mostafa Saleh <smostafa@google.com>
13. **[08-19 21:51]** [PATCH v4 12/28] KVM: arm64: iommu: Support DABT for IOMMU
   - 发件人: Mostafa Saleh <smostafa@google.com>
14. **[08-19 21:51]** [PATCH v4 13/28] iommu/arm-smmu-v3-kvm: Add SMMUv3 driver
   - 发件人: Mostafa Saleh <smostafa@google.com>
15. **[08-19 21:51]** [PATCH v4 14/28] iommu/arm-smmu-v3: Add KVM mode in the driver
   - 发件人: Mostafa Saleh <smostafa@google.com>
16. **[08-19 21:51]** [PATCH v4 15/28] iommu/arm-smmu-v3: Load the driver later in KVM mode
   - 发件人: Mostafa Saleh <smostafa@google.com>
17. **[08-19 21:51]** [PATCH v4 16/28] iommu/arm-smmu-v3-kvm: Create array for hyp SMMUv3
   - 发件人: Mostafa Saleh <smostafa@google.com>
18. **[08-19 21:51]** [PATCH v4 17/28] iommu/arm-smmu-v3-kvm: Take over SMMUs
   - 发件人: Mostafa Saleh <smostafa@google.com>
19. **[08-19 21:51]** [PATCH v4 18/28] iommu/arm-smmu-v3-kvm: Probe SMMU HW
   - 发件人: Mostafa Saleh <smostafa@google.com>
20. **[08-19 21:51]** [PATCH v4 19/28] iommu/arm-smmu-v3-kvm: Add MMIO emulation
   - 发件人: Mostafa Saleh <smostafa@google.com>
21. **[08-19 21:51]** [PATCH v4 20/28] iommu/arm-smmu-v3-kvm: Shadow the command queue
   - 发件人: Mostafa Saleh <smostafa@google.com>
22. **[08-19 21:51]** [PATCH v4 21/28] iommu/arm-smmu-v3-kvm: Add CMDQ functions
   - 发件人: Mostafa Saleh <smostafa@google.com>
23. **[08-19 21:51]** [PATCH v4 22/28] iommu/arm-smmu-v3-kvm: Emulate CMDQ for host
   - 发件人: Mostafa Saleh <smostafa@google.com>
24. **[08-19 21:51]** [PATCH v4 23/28] iommu/arm-smmu-v3-kvm: Shadow stream table
   - 发件人: Mostafa Saleh <smostafa@google.com>
25. **[08-19 21:51]** [PATCH v4 24/28] iommu/arm-smmu-v3-kvm: Shadow STEs
   - 发件人: Mostafa Saleh <smostafa@google.com>
26. **[08-19 21:51]** [PATCH v4 25/28] iommu/arm-smmu-v3-kvm: Emulate GBPA
   - 发件人: Mostafa Saleh <smostafa@google.com>
27. **[08-19 21:51]** [PATCH v4 26/28] iommu/arm-smmu-v3-kvm: Support io-pgtable
   - 发件人: Mostafa Saleh <smostafa@google.com>
28. **[08-19 21:51]** [PATCH v4 27/28] iommu/arm-smmu-v3-kvm: Shadow the CPU stage-2 page table
   - 发件人: Mostafa Saleh <smostafa@google.com>
29. **[08-19 21:51]** [PATCH v4 28/28] iommu/arm-smmu-v3-kvm: Enable nesting
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 4: [PATCH v6 00/24] Tracefs support for pKVM

**📧 邮件数**: 25 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 21 Aug 2025 09:13:48 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 pKVM 的 Tracefs 支持的补丁系列（[PATCH v6 00/24]），主要涉及如何在受保护模式下为 hypervisor 提供调试和性能分析工具。以下是讨论的主要内容：

1. **原始补丁/问题的内容**：
   - 该补丁系列引入了一个新的通用方法，用于创建远程事件和远程缓冲区，并为 pKVM hypervisor 添加支持。补丁中包括了环形缓冲区的设置、Tracefs 的集成以及事件的创建。

2. **之前讨论的要点**：
   - 之前的讨论集中在如何实现远程环形缓冲区的功能，确保 hypervisor 能够将事件写入 Tracefs 兼容的环形缓冲区。同时，补丁还解决了与现有内核功能的兼容性问题。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论中，Vincent Donnefort 提出了多个补丁，涵盖了环形缓冲区的统计信息、Tracefs 的远程支持、事件的创建和处理等。特别是，补丁系列中引入了新的事件宏（HYP_EVENT()），简化了事件的声明过程。此外，添加了自测试事件支持，以便在用户空间触发事件并进行测试。最后，讨论还包括了对 pKVM hypervisor 的时钟同步和重置功能的实现。

整体来看，本周的讨论和补丁推进了 pKVM 在 Tracefs 支持方面的进展，为未来的调试和性能分析奠定了基础。

#### 📝 邮件列表

1. **[08-21 09:13]** [PATCH v6 00/24] Tracefs support for pKVM
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
2. **[08-21 09:13]** [PATCH v6 01/24] ring-buffer: Add page statistics to the meta-page
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
3. **[08-21 09:13]** [PATCH v6 02/24] ring-buffer: Introduce ring-buffer remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[08-21 09:13]** [PATCH v6 03/24] tracing: Introduce trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[08-21 09:13]** [PATCH v6 04/24] tracing: Add reset to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[08-21 09:13]** [PATCH v6 05/24] tracing: Add init callback to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[08-21 09:13]** [PATCH v6 06/24] tracing: Add events to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
8. **[08-21 09:13]** [PATCH v6 07/24] tracing: Add events/ root files to trace remotes
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
9. **[08-21 09:13]** [PATCH v6 08/24] tracing: Add helpers to create trace remote events
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
10. **[08-21 09:13]** [PATCH v6 09/24] ring-buffer: Export buffer_data_page and macros
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
11. **[08-21 09:13]** [PATCH v6 10/24] tracing: Introduce simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
12. **[08-21 09:13]** [PATCH v6 11/24] tracing: Add a trace remote module for testing
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
13. **[08-21 09:14]** [PATCH v6 12/24] tracing: selftests: Add trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
14. **[08-21 09:14]** [PATCH v6 13/24] tracing: load/unload page callbacks for simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
15. **[08-21 09:14]** [PATCH v6 14/24] tracing: Check for undefined symbols in simple_ring_buffer
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
16. **[08-21 09:14]** [PATCH v6 15/24] KVM: arm64: Support unaligned fixmap in the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
17. **[08-21 09:14]** [PATCH v6 16/24] KVM: arm64: Add clock support for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
18. **[08-21 09:14]** [PATCH v6 17/24] KVM: arm64: Add tracing capability for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
19. **[08-21 09:14]** [PATCH v6 18/24] KVM: arm64: Add trace remote for the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
20. **[08-21 09:14]** [PATCH v6 19/24] KVM: arm64: Sync boot clock with the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
21. **[08-21 09:14]** [PATCH v6 20/24] KVM: arm64: Add trace reset to the pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
22. **[08-21 09:14]** [PATCH v6 21/24] KVM: arm64: Add event support to the pKVM hyp and
 trace remote
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
23. **[08-21 09:14]** [PATCH v6 22/24] KVM: arm64: Add hyp_enter/hyp_exit events to pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
24. **[08-21 09:14]** [PATCH v6 23/24] KVM: arm64: Add selftest event support to pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
25. **[08-21 09:14]** [PATCH v6 24/24] tracing: selftests: Add pKVM trace remote tests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 5: [PATCH v3 0/6] KVM: arm64: FEAT_RASv1p1 support and RAS selection

**📧 邮件数**: 18 | **👥 参与者**: 5 | **📅 开始时间**: Sun, 17 Aug 2025 21:21:52 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FEAT_RASv1p1 的一系列补丁（patch）。这些补丁旨在填补现有的 RAS（Reliability, Availability, and Serviceability）功能的空白，确保在适当的硬件上能够正确处理 RASv1p1 相关的寄存器。

在历史讨论中，Marc Zyngier 提出了六个补丁，主要内容包括：
1. 添加表示 FEAT_RASv1p1 的能力。
2. 处理 RASv1p1 寄存器，确保在虚拟机中能够正确访问。
3. 忽略由 L1 客户机的 EL2 设置的 HCR_EL2.FIEN，以防止 EL1 客户机注入错误记录。
4. 使 ID_AA64PFR0_EL1.RAS 可写，以便在不同配置的系统间迁移虚拟机。
5. 使 ID_AA64PFR1_EL1.RAS_frac 可写。
6. 移除不可靠的 ARM64_FEATURE_MASK() 宏。

在本周的新讨论中，多个参与者对这些补丁进行了审查并给予了认可（Reviewed-by），包括 Cornelia Huck 和 Joey Gouly。Ben Horgan 提出了一些关于补丁实现细节的疑问，并与 Marc Zyngier 进行了讨论，最终确认了补丁的正确性。最后，Marc Zyngier 表示这些补丁已被应用到修复中，标志着该功能的进一步推进。

#### 📝 邮件列表

1. **[08-17 21:21]** [PATCH v3 0/6] KVM: arm64: FEAT_RASv1p1 support and RAS selection
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[08-17 21:21]** [PATCH v3 1/6] arm64: Add capability denoting FEAT_RASv1p1
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[08-17 21:21]** [PATCH v3 2/6] KVM: arm64: Handle RASv1p1 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[08-17 21:21]** [PATCH v3 3/6] KVM: arm64: Ignore HCR_EL2.FIEN set by L1 guest's EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[08-17 21:21]** [PATCH v3 4/6] KVM: arm64: Make ID_AA64PFR0_EL1.RAS writable
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[08-17 21:21]** [PATCH v3 5/6] KVM: arm64: Make ID_AA64PFR1_EL1.RAS_frac writable
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[08-17 21:21]** [PATCH v3 6/6] KVM: arm64: Get rid of ARM64_FEATURE_MASK()
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[08-18 14:32]** Re: [PATCH v3 1/6] arm64: Add capability denoting FEAT_RASv1p1
   - 发件人: Cornelia Huck <cohuck@redhat.com>
9. **[08-18 14:34]** Re: [PATCH v3 2/6] KVM: arm64: Handle RASv1p1 registers
   - 发件人: Cornelia Huck <cohuck@redhat.com>
10. **[08-18 14:37]** Re: [PATCH v3 4/6] KVM: arm64: Make ID_AA64PFR0_EL1.RAS writable
   - 发件人: Cornelia Huck <cohuck@redhat.com>
11. **[08-18 14:43]** Re: [PATCH v3 5/6] KVM: arm64: Make ID_AA64PFR1_EL1.RAS_frac writable
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[08-19 11:24]** Re: [PATCH v3 3/6] KVM: arm64: Ignore HCR_EL2.FIEN set by L1 guest's
 EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
13. **[08-21 12:29]** Re: [PATCH v3 6/6] KVM: arm64: Get rid of ARM64_FEATURE_MASK()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
14. **[08-21 14:13]** Re: [PATCH v3 2/6] KVM: arm64: Handle RASv1p1 registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
15. **[08-21 14:37]** Re: [PATCH v3 2/6] KVM: arm64: Handle RASv1p1 registers
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[08-21 14:43]** Re: [PATCH v3 6/6] KVM: arm64: Get rid of ARM64_FEATURE_MASK()
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[08-21 14:44]** Re: [PATCH v3 2/6] KVM: arm64: Handle RASv1p1 registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
18. **[08-21 17:01]** Re: [PATCH v3 0/6] KVM: arm64: FEAT_RASv1p1 support and RAS selection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 6: [PATCH v3 0/5] initialize SCTRL2_ELx

**📧 邮件数**: 18 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 13 Aug 2025 13:01:13 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Linux 内核的一个补丁系列，主要涉及对 ARM 架构中 SCTLR2_ELx 寄存器的初始化支持。该补丁系列共有五个部分，旨在为 ARMv8.8/ARMv9.3 及以上版本提供对 SCTLR2_ELx 寄存器的支持，尽管当前 Linux 并不严格要求修改这些寄存器，但未来的架构特性将需要配置这些寄存器中的控制位。

在历史讨论中，Yeoreum Yun 提出了五个补丁，分别涵盖了使 SCTLR2_EL1 可访问、在启动时初始化 SCTLR2_ELx、在 CPU 挂起和恢复时保存/恢复 SCTLR2_EL1、在软重启时初始化 SCTLR2_EL1，以及为每个任务设置 SCTLR2_EL1 的功能。这些补丁的主要目的是确保在不同情况下寄存器的状态一致性，以避免潜在的系统不稳定。

在本周的新讨论中，Dave Martin 对补丁提出了一些具体的代码改进建议，包括命名规范、代码可读性和性能优化等。他指出了一些代码中的潜在问题，并建议在实现中遵循更清晰的逻辑。此外，Yeoreum Yun 对于 Dave 的反馈表示感谢，并承诺将进行相应的修改。整体来看，本周的讨论集中在补丁的细节优化和代码质量提升上。

#### 📝 邮件列表

1. **[08-13 13:01]** [PATCH v3 0/5] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[08-13 13:01]** [PATCH v3 1/5] arm64: make SCTLR2_EL1 accessible
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[08-13 13:01]** [PATCH v3 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[08-13 13:01]** [PATCH v3 3/5] arm64: save/restore SCTLR2_EL1 when cpu_suspend()/resume()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[08-13 13:01]** [PATCH v3 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[08-13 13:01]** [PATCH v3 5/5] arm64: make the per-task SCTLR2_EL1
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[08-20 16:10]** Re: [PATCH v3 1/5] arm64: make SCTLR2_EL1 accessible
   - 发件人: Dave Martin <Dave.Martin@arm.com>
8. **[08-20 16:10]** Re: [PATCH v3 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Dave Martin <Dave.Martin@arm.com>
9. **[08-20 16:11]** Re: [PATCH v3 3/5] arm64: save/restore SCTLR2_EL1 when
 cpu_suspend()/resume()
   - 发件人: Dave Martin <Dave.Martin@arm.com>
10. **[08-20 16:11]** Re: [PATCH v3 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Dave Martin <Dave.Martin@arm.com>
11. **[08-20 16:11]** Re: [PATCH v3 5/5] arm64: make the per-task SCTLR2_EL1
   - 发件人: Dave Martin <Dave.Martin@arm.com>
12. **[08-20 16:11]** Re: [PATCH v3 0/5] initialize SCTRL2_ELx
   - 发件人: Dave Martin <Dave.Martin@arm.com>
13. **[08-20 18:18]** Re: [PATCH v3 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
14. **[08-20 18:22]** Re: [PATCH v3 3/5] arm64: save/restore SCTLR2_EL1 when
 cpu_suspend()/resume()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
15. **[08-20 18:32]** Re: [PATCH v3 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
16. **[08-20 18:34]** Re: [PATCH v3 5/5] arm64: make the per-task SCTLR2_EL1
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
17. **[08-20 19:51]** Re: [PATCH v3 1/5] arm64: make SCTLR2_EL1 accessible
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
18. **[08-21 11:14]** Re: [PATCH v3 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 7: [PATCH 0/4] arm64/sysreg: Clean up TCR_XXX field macros

**📧 邮件数**: 18 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 18 Aug 2025 10:27:55 +0530

#### 🤖 AI 总结

本邮件线程讨论的主题是对 ARM64 架构中的 TCR（Translation Control Register）相关宏的清理和更新，主要涉及四个补丁（PATCH 0/4 到 PATCH 4/4）。

1. **原始补丁内容**：
   - 补丁旨在清理和更新 TCR_EL1、TCR_EL2 和 VTCR_EL2 的字段宏，确保它们符合最新的 ARM 架构文档（DDI 0487 7.B）。补丁包括对相关寄存器的定义和替换，且不引入功能性变化。

2. **之前讨论要点**：
   - 之前的讨论集中在如何有效地替换和清理现有的 TCR 宏，确保代码的一致性和可读性。参与者对使用的枚举类型提出了建议，认为应使用有序的枚举而非无符号枚举，以提高代码的可维护性。

3. **本周的新讨论与进展**：
   - 本周的讨论中，参与者 Mark Rutland 对补丁提出了具体的改进建议，指出在某些情况下应使用枚举类型而非字段定义，并强调了代码的可读性问题。此外，Marc Zyngier 提出了对寄存器定义准确性和完整性的关注，建议使用更可靠的工具来生成寄存器描述。最终，Anshuman Khandual 表示将根据反馈进行相应的修改。

总体来看，本周的讨论进一步推动了对 ARM64 TCR 宏的清理工作，确保代码的准确性和一致性，同时也反映了开发者在维护代码质量方面的共同努力。

#### 📝 邮件列表

1. **[08-18 10:27]** [PATCH 0/4] arm64/sysreg: Clean up TCR_XXX field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
2. **[08-18 10:27]** [PATCH 1/4] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
3. **[08-18 10:27]** [PATCH 2/4] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
4. **[08-18 10:27]** [PATCH 3/4] arm64/sysreg: Add TCR_EL2 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
5. **[08-18 10:27]** [PATCH 4/4] arm64/sysreg: Add VTCR_EL2 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
6. **[08-18 10:11]** Re: [PATCH 1/4] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Mark Rutland <mark.rutland@arm.com>
7. **[08-18 10:17]** Re: [PATCH 3/4] arm64/sysreg: Add TCR_EL2 register
   - 发件人: Mark Rutland <mark.rutland@arm.com>
8. **[08-18 10:22]** Re: [PATCH 4/4] arm64/sysreg: Add VTCR_EL2 register
   - 发件人: Mark Rutland <mark.rutland@arm.com>
9. **[08-18 16:43]** Re: [PATCH 3/4] arm64/sysreg: Add TCR_EL2 register
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[08-18 16:46]** Re: [PATCH 2/4] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[08-19 09:13]** Re: [PATCH 1/4] arm64/sysreg: Update TCR_EL1 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
12. **[08-19 09:16]** Re: [PATCH 3/4] arm64/sysreg: Add TCR_EL2 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
13. **[08-19 09:54]** Re: [PATCH 4/4] arm64/sysreg: Add VTCR_EL2 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
14. **[08-19 11:28]** Re: [PATCH 3/4] arm64/sysreg: Add TCR_EL2 register
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
15. **[08-19 12:16]** Re: [PATCH 2/4] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>
16. **[08-19 09:12]** Re: [PATCH 2/4] arm64/sysreg: Replace TCR_EL1 field macros
   - 发件人: Marc Zyngier <maz@kernel.org>
17. **[08-19 09:29]** Re: [PATCH 3/4] arm64/sysreg: Add TCR_EL2 register
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[08-19 09:35]** Re: [PATCH 4/4] arm64/sysreg: Add VTCR_EL2 register
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH v15 0/6] KVM: arm64: Provide guest support for GCS

**📧 邮件数**: 17 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 20 Aug 2025 15:14:40 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 Guarded Control Stack（GCS）的补丁系列（PATCH v15 0/6）。GCS 是一种硬件保护栈的特性，旨在增强对返回导向编程（ROP）攻击的防护，并简化应用程序的调用栈收集。

### 原始补丁内容
补丁系列的主要目标是为 KVM 客户端提供 GCS 支持，包括对 GCS 操作的管理、异常处理以及相关寄存器的配置。补丁还修复了 S1PIE 特性，这是 GCS 的依赖项。

### 之前讨论要点
在之前的讨论中，参与者们关注了 GCS 特性的实现细节，包括如何在 KVM 中管理 GCS 寄存器、异常转发以及对 GCS 操作的细粒度控制。补丁的多个版本中，开发者们不断调整和优化代码，以确保 GCS 的有效性和安全性。

### 本周新讨论和进展
本周的讨论集中在补丁的具体实现上，包括：
1. **GCS 寄存器的管理**：确保 GCS 寄存器在上下文切换时被正确处理，并向虚拟机监控器（VMM）暴露。
2. **异常处理**：讨论了如何将 GCS 生成的异常从 EL0 转发到 EL2，以便在嵌套客户机中正确处理。
3. **PSTATE.EXLOCK 的管理**：实现了在进入异常时对 PSTATE.EXLOCK 的设置逻辑。
4. **GCS 特性的启用**：补丁允许在客户机中启用 GCS 特性，并添加了相关的自测试代码以验证新寄存器。

参与者们还对补丁的细节进行了审查和讨论，提出了对代码可读性和功能完整性的建议。整体上，讨论表明开发者们在不断推进 GCS 支持的实现，确保其在 KVM 中的有效性和安全性。

#### 📝 邮件列表

1. **[08-20 15:14]** [PATCH v15 0/6] KVM: arm64: Provide guest support for GCS
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[08-20 15:14]** [PATCH v15 1/6] arm64/gcs: Ensure FGTs for EL1 GCS instructions
 are disabled
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[08-20 15:14]** [PATCH v15 2/6] KVM: arm64: Manage GCS access and registers for
 guests
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[08-20 15:14]** [PATCH v15 3/6] KVM: arm64: Forward GCS exceptions to nested
 guests
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[08-20 15:14]** [PATCH v15 4/6] KVM: arm64: Set PSTATE.EXLOCK when entering an
 exception
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[08-20 15:14]** [PATCH v15 5/6] KVM: arm64: Allow GCS to be enabled for guests
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[08-20 15:14]** [PATCH v15 6/6] KVM: selftests: arm64: Add GCS registers to
 get-reg-list
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[08-20 22:06]** Re: [PATCH v15 2/6] KVM: arm64: Manage GCS access and registers for guests
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[08-20 23:02]** Re: [PATCH v15 4/6] KVM: arm64: Set PSTATE.EXLOCK when entering an exception
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[08-20 23:13]** Re: [PATCH v15 2/6] KVM: arm64: Manage GCS access and registers for
 guests
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[08-20 23:15]** Re: [PATCH v15 3/6] KVM: arm64: Forward GCS exceptions to nested guests
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[08-20 23:18]** Re: [PATCH v15 5/6] KVM: arm64: Allow GCS to be enabled for guests
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[08-20 23:24]** Re: [PATCH v15 1/6] arm64/gcs: Ensure FGTs for EL1 GCS instructions are disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[08-20 23:28]** Re: [PATCH v15 1/6] arm64/gcs: Ensure FGTs for EL1 GCS instructions are disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
15. **[08-20 23:30]** Re: [PATCH v15 0/6] KVM: arm64: Provide guest support for GCS
   - 发件人: Marc Zyngier <maz@kernel.org>
16. **[08-21 21:44]** Re: [PATCH v15 4/6] KVM: arm64: Set PSTATE.EXLOCK when entering an
 exception
   - 发件人: Mark Brown <broonie@kernel.org>
17. **[08-21 22:25]** Re: [PATCH v15 3/6] KVM: arm64: Forward GCS exceptions to nested
 guests
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 9: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs

**📧 邮件数**: 12 | **👥 参与者**: 5 | **📅 开始时间**: Wed,  6 Aug 2025 12:56:22 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）对中介虚拟性能监控单元（mediated vPMUs）支持的补丁系列，具体为 [PATCH v5 00/44]。该补丁旨在改进 KVM 在虚拟化环境中对性能监控的支持，尤其是在处理来宾（guest）上下文时的性能监控中断（PMI）管理。

在历史讨论中，参与者主要集中在补丁的设计和实现细节上，特别是如何在来宾上下文加载和卸载时安全地切换 LVTPC（本地向量定时器控制寄存器）。Sean Christopherson 提出了补丁的初步设计，并与 Peter Zijlstra 等人讨论了实现中的潜在问题和解决方案，包括对中介 PMU 的处理和对性能监控中断的管理。

在本周的新讨论中，Peter Zijlstra 和 Sean Christopherson 进一步探讨了在来宾处理 PMI 时进行 VM-exit 的安全性问题，强调了在处理 PMU 状态时需要注意的细节。此外，Xudong Hao 提供了对补丁的测试结果，表明在多个 Intel 平台上进行的性能测试均未发现问题，验证了中介 vPMU 和传统性能监控的兼容性。

总的来说，该邮件线程展示了 KVM 对中介 vPMUs 支持的持续改进，以及社区成员在实现过程中的积极讨论与协作。

#### 📝 邮件列表

1. **[08-06 12:56]** [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[08-06 12:56]** [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI vector
 on guest load/put context
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-06 12:56]** [PATCH v5 16/44] KVM: Add a simplified wrapper for registering perf callbacks
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[08-15 13:39]** Re: [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI
 vector on guest load/put context
   - 发件人: Peter Zijlstra <peterz@infradead.org>
5. **[08-15 08:41]** Re: [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI
 vector on guest load/put context
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[08-15 08:55]** Re: [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI
 vector on guest load/put context
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[08-18 16:32]** Re: [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI
 vector on guest load/put context
   - 发件人: Peter Zijlstra <peterz@infradead.org>
8. **[08-18 08:25]** Re: [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI
 vector on guest load/put context
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[08-18 18:12]** Re: [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI
 vector on guest load/put context
   - 发件人: Peter Zijlstra <peterz@infradead.org>
10. **[08-18 13:07]** Re: [PATCH v5 09/44] perf/x86: Switch LVTPC to/from mediated PMI
 vector on guest load/put context
   - 发件人: Liang, Kan <kan.liang@linux.intel.com>
11. **[08-22 16:12]** Re: [PATCH v5 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Hao, Xudong <xudong.hao@intel.com>
12. **[08-22 16:02]** Re: [PATCH v5 16/44] KVM: Add a simplified wrapper for registering
 perf callbacks
   - 发件人: Anup Patel <anup@brainfault.org>

---

### Thread 10: [PATCH v6 0/5] support FEAT_LSUI and apply it on futex atomic ops

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 11 Aug 2025 17:36:30 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于支持 Armv9.6 的 FEAT_LSUI 特性，并将其应用于 futex 原子操作的补丁集（PATCH v6 0/5）。该补丁的核心内容是通过 FEAT_LSUI 提供的加载/存储指令，允许内核在不清除 PSTATE.PAN 位的情况下访问用户内存，从而简化了当前使用的 ll/sc 指令实现。

在历史讨论中，参与者 Yeoreum Yun 详细介绍了补丁的结构，包括添加 CPU 特性支持、向来宾暴露 FEAT_LSUI 等。Catalin Marinas 提出了关于用户和内核在标签检查方面可能存在不同设置的关注，强调了在使用 FEAT_LSUI 指令时需要考虑 MTE（内存标签扩展）的影响。

在本周的新讨论中，Catalin 和 Yeoreum 继续探讨了在使用 LSUI 指令时是否需要启用 TCO（标签检查覆盖）。Catalin 指出，futex 使用 LSUI 时应启用 TCO，以确保一致性，避免在内核访问用户内存时出现不一致的标签检查行为。Yeoreum 最终确认了这一点，表示在使用 LSUI 指令时不需要启用 TCO。

总体来看，本周的讨论进一步澄清了补丁的实现细节，特别是在处理用户内存访问时的标签检查机制。

#### 📝 邮件列表

1. **[08-11 17:36]** [PATCH v6 0/5] support FEAT_LSUI and apply it on futex atomic ops
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[08-11 17:36]** [PATCH v6 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[08-15 18:02]** Re: [PATCH v6 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
4. **[08-16 13:30]** Re: [PATCH v6 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[08-16 15:57]** Re: [PATCH v6 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[08-18 19:35]** Re: [PATCH v6 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
7. **[08-18 20:53]** Re: [PATCH v6 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[08-19 09:38]** Re: [PATCH v6 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[08-19 10:11]** Re: [PATCH v6 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[08-19 15:29]** Re: [PATCH v6 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
11. **[08-19 16:15]** Re: [PATCH v6 5/5] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 11: [PATCH v5 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 8 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 18 Aug 2025 14:47:59 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 Armv8.7 架构新增的 FEAT_{LS64, LS64_V} 特性及其相关测试的支持。该特性引入了单拷贝原子 64 字节的加载和存储指令，旨在提升用户空间驱动的性能。

**原始 patch/问题的内容**：
Yicong Yang 提出了一个包含 7 个补丁的系列，主要目的是为 Armv8.7 的 FEAT_{LS64, LS64_V} 提供支持，包括在 CPU 特性列表中识别和启用这些特性，向用户空间暴露支持信息，并处理虚拟机中的不支持内存访问的异常。

**之前讨论要点**：
在历史讨论中，补丁的基础结构和设计理念已经被初步确立，主要集中在如何有效地处理虚拟机中的内存访问异常以及如何将这些新特性集成到现有的 KVM 架构中。

**本周的新讨论、进展或结论**：
本周的讨论主要围绕补丁的具体实现和测试进展。Yicong Yang 提交了多个补丁，涵盖了对 FEAT_{LS64, LS64_V} 的支持、KVM 中的相关文档更新、以及对这些特性的自测试。补丁中还包括对用户空间如何处理这些指令的详细说明，并确保在不支持的内存类型上触发数据中止异常。测试结果表明，相关指令可以在支持这些特性的系统上正常执行，没有收到 SIGILL 信号，显示出补丁的有效性和稳定性。整体来看，补丁系列的进展顺利，预计将为 Linux 内核的虚拟化性能带来显著提升。

#### 📝 邮件列表

1. **[08-18 14:47]** [PATCH v5 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Yicong Yang <yangyicong@huawei.com>
2. **[08-18 14:48]** [PATCH v5 1/7] KVM: arm64: Add exit to userspace on {LD,ST}64B* outside of memslots
   - 发件人: Yicong Yang <yangyicong@huawei.com>
3. **[08-18 14:48]** [PATCH v5 2/7] KVM: arm64: Add documentation for KVM_EXIT_ARM_LDST64B
   - 发件人: Yicong Yang <yangyicong@huawei.com>
4. **[08-18 14:48]** [PATCH v5 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Yicong Yang <yangyicong@huawei.com>
5. **[08-18 14:48]** [PATCH v5 4/7] arm64: Provide basic EL2 setup for FEAT_{LS64, LS64_V} usage at EL0/1
   - 发件人: Yicong Yang <yangyicong@huawei.com>
6. **[08-18 14:48]** [PATCH v5 5/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
7. **[08-18 14:48]** [PATCH v5 6/7] KVM: arm64: Enable FEAT_{LS64, LS64_V} in the supported guest
   - 发件人: Yicong Yang <yangyicong@huawei.com>
8. **[08-18 14:48]** [PATCH v5 7/7] kselftest/arm64: Add HWCAP test for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>

---

### Thread 12: [PATCH v11 0/6] KVM: arm64: Support FF-A 1.2

**📧 邮件数**: 7 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 20 Aug 2025 01:10:04 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A（Firmware Framework for Arm）1.2 版本的补丁集。补丁集包含六个部分，主要目标是引入新的 SEND_DIRECT2 ABI，并确保主机与虚拟机之间的兼容性。

在历史讨论中，补丁的背景是 FF-A 1.2 规范的引入，特别是新的 SEND_DIRECT2 ABI 允许使用 x4-x17 寄存器进行消息传递。补丁集的设计旨在防止主机使用低于已协商版本的 FF-A 版本，以确保虚拟机能够正确处理消息。

本周的新讨论中，Per Larsen 提出了多个补丁的具体实现细节，包括：
1. **补丁 1**：修正主机版本降级尝试时的返回值，确保版本协商后保持锁定。
2. **补丁 2**：在 FF-A 初始化和主机处理程序中使用 SMCCC 1.2，以支持更多返回值。
3. **补丁 3**：将 FFA_NOTIFICATION_* 接口标记为不支持，防止其被传递到信任区（TZ）。
4. **补丁 4**：将 FF-A 1.2 的可选接口标记为不支持，以避免被代理。
5. **补丁 5**：在处理 FFA_FEATURE 调用时掩码响应，确保返回的最小缓冲区大小正确。
6. **补丁 6**：将支持的 FF-A 版本提升至 1.2，以启用新的消息接口。

所有补丁均获得了 Will Deacon 的认可，显示出社区对这一系列改进的支持。整体来看，这些补丁的实施将增强 KVM 在 arm64 平台上的功能和稳定性。

#### 📝 邮件列表

1. **[08-20 01:10]** [PATCH v11 0/6] KVM: arm64: Support FF-A 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[08-20 01:10]** [PATCH v11 1/6] KVM: arm64: Correct return value on host version
 downgrade attempt
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[08-20 01:10]** [PATCH v11 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[08-20 01:10]** [PATCH v11 3/6] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[08-20 01:10]** [PATCH v11 4/6] KVM: arm64: Mark optional FF-A 1.2 interfaces as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[08-20 01:10]** [PATCH v11 5/6] KVM: arm64: Mask response to FFA_FEATURE call
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[08-20 01:10]** [PATCH v11 6/6] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>

---

### Thread 13: [PATCH v4 0/5] initialize SCTRL2_ELx

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 21 Aug 2025 18:24:03 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 Linux 中初始化 SCTLR2_ELx 寄存器的补丁（PATCH v4 0/5）。该补丁系列旨在为 ARM 架构的 SCTLR2_ELx 寄存器提供初步支持，该功能在 ARMv8.8/ARMv9.3 版本中为可选，ARMv8.9/ARMv9.4 版本中为强制要求。

在历史讨论中，补丁经历了多个版本的修改，主要包括合并函数、修复寄存器设置错误以及在 CPU 启动时初始化 SCTLR2_ELx 寄存器等。补丁的目标是确保在系统启动和 CPU 休眠/恢复过程中，SCTLR2_ELx 寄存器的值能够正确保存和恢复，以避免系统行为异常。

本周的新讨论中，Yeoreum Yun 提出了五个具体补丁，涵盖了以下内容：
1. 使 SCTLR2_EL1 可访问，并确保在初始化 EL2 时设置相关位。
2. 在 CPU 启动时初始化 SCTLR2_ELx 寄存器，以防止未初始化值导致的系统问题。
3. 在 CPU 休眠和恢复过程中保存和恢复 SCTLR2_EL1 的值。
4. 在 kexec 启动新内核之前初始化 SCTLR2_ELx 寄存器，避免使用任意值。
5. 支持按任务维护 SCTLR2_EL1，以便未来能够配置与 FEAT_CPA2 相关的字段。

这些补丁的实施将为未来的架构特性提供支持，并确保系统的稳定性和一致性。

#### 📝 邮件列表

1. **[08-21 18:24]** [PATCH v4 0/5] initialize SCTRL2_ELx
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[08-21 18:24]** [PATCH v4 1/5] arm64: make SCTLR2_EL1 accessible
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[08-21 18:24]** [PATCH v4 2/5] arm64: initialise SCTLR2_ELx register at boot time
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[08-21 18:24]** [PATCH v4 3/5] arm64: save/restore SCTLR2_EL1 when cpu_suspend()/resume()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[08-21 18:24]** [PATCH v4 4/5] arm64: initialise SCTLR2_EL1 at cpu_soft_restart()
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[08-21 18:24]** [PATCH v4 5/5] arm64: make the per-task SCTLR2_EL1
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 14: [STABLE] [PATCH] KVM: arm64: Fix kernel BUG() due to bad backport of FPSIMD/SVE/SME fix

**📧 邮件数**: 5 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 22 Aug 2025 15:04:02 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于修复 KVM 在 arm64 架构下由于 FPSIMD/SVE/SME 修复的错误回溯而导致的内核 BUG() 问题。原始的补丁由 Will Deacon 提出，旨在解决在 `fpsimd_save_and_flush_cpu_state()` 函数中未禁用中断的问题，这可能导致在保存主机浮点上下文时触发 BUG_ON(!may_use_simd()) 错误。

在历史讨论中，补丁指出，稳定内核版本缺少某些修复（如 9b19700e623f），使得在执行 `fpsimd_save_and_flush_cpu_state()` 时中断仍然处于启用状态，从而引发了实际使用中的内核错误。为了解决此问题，补丁建议使用软中断安全的 `{get,put}_cpu_fpsimd_context()` 帮助函数。

在本周的新讨论中，Greg Kroah-Hartman 确认已将该补丁加入到多个稳定内核版本（5.15、6.1 和 6.6）的稳定树中，表示补丁已成功应用并解决了相关问题。这标志着该问题的修复工作已得到认可并正式发布。

#### 📝 邮件列表

1. **[08-22 15:04]** [STABLE] [PATCH] KVM: arm64: Fix kernel BUG() due to bad backport of FPSIMD/SVE/SME fix
   - 发件人: Will Deacon <will@kernel.org>
2. **[08-22 16:25]** Re: [STABLE] [PATCH] KVM: arm64: Fix kernel BUG() due to bad
 backport of FPSIMD/SVE/SME fix
   - 发件人: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
3. **[08-22 16:25]** Patch "KVM: arm64: Fix kernel BUG() due to bad backport of FPSIMD/SVE/SME fix" has been added to the 5.15-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>
4. **[08-22 16:25]** Patch "KVM: arm64: Fix kernel BUG() due to bad backport of FPSIMD/SVE/SME fix" has been added to the 6.1-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>
5. **[08-22 16:25]** Patch "KVM: arm64: Fix kernel BUG() due to bad backport of FPSIMD/SVE/SME fix" has been added to the 6.6-stable tree
   - 发件人: gregkh <gregkh@linuxfoundation.org>

---

### Thread 15: [PATCH v2 0/2] KVM: arm64: Reschedule as needed when destroying the
 stage-2 page-tables

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 20 Aug 2025 16:22:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在处理 ARM64 架构的 stage-2 页表销毁时的调度问题。原始的 patch 包含两个部分：第一部分是将 `kvm_pgtable_stage2_destroy()` 函数拆分为两个独立的函数，以便在销毁页表时能够分块处理；第二部分则是在销毁过程中引入条件调度，以避免长时间占用 CPU 导致的调度警告。

在历史讨论中，参与者提到，当一个完全映射的 128G 虚拟机被突然销毁时，系统会出现调度警告，主要是由于页表遍历操作耗时较长，特别是在配置为不强制抢占的内核（如 `CONFIG_PREEMPT_NONE=y`）下。为了解决这个问题，建议将页表遍历分成更小的范围，并在每个范围之间调用 `cond_resched()`。

在本周的新讨论中，Raghavendra Rao Ananta 提出了具体的实现方案，并在邮件中详细描述了 patch 的内容和改动。Oliver Upton 对该 patch 表示认可，并已将其应用于修复补丁中，确认了两个 patch 的有效性和必要性。这标志着该问题的解决方案得到了认可并进入了代码库。

#### 📝 邮件列表

1. **[08-20 16:22]** [PATCH v2 0/2] KVM: arm64: Reschedule as needed when destroying the
 stage-2 page-tables
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[08-20 16:22]** [PATCH v2 1/2] KVM: arm64: Split kvm_pgtable_stage2_destroy()
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
3. **[08-20 16:22]** [PATCH v2 2/2] KVM: arm64: Reschedule as needed when destroying the
 stage-2 page-tables
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
4. **[08-21 17:02]** Re: [PATCH v2 0/2] KVM: arm64: Reschedule as needed when destroying the stage-2 page-tables
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 16: [PATCH v3 0/3] arm64: Support FEAT_LSFE (Large System Float
 Extension)

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 18 Aug 2025 20:21:17 +0100

#### 🤖 AI 总结

本邮件线程讨论了对 ARM64 架构的 FEAT_LSFE（大系统浮点扩展）功能的支持，主要通过三个补丁进行实现。

1. **原始补丁内容**：补丁旨在为 ARM64 架构添加对 FEAT_LSFE 的支持，该特性从 v9.5 开始是可选的，提供原子浮点内存操作。补丁的主要目标是为用户空间提供硬件能力标志（hwcap），并允许 KVM 客户端访问相关的 ID 寄存器字段。

2. **之前讨论要点**：在历史讨论中，补丁的前几个版本进行了多次修改，主要集中在修复 hwcap 测试的结果和代码重构上。补丁的目的明确，即使内核当前没有直接使用该特性，也要为用户空间提供发现机制。

3. **本周新讨论与进展**：本周的讨论中，Mark Brown 提出了三个补丁的具体实现：
   - 第一个补丁添加了 hwcap 标志以支持 FEAT_LSFE。
   - 第二个补丁使 KVM 能够将 FEAT_LSFE 暴露给虚拟机客户，以便它们可以识别该特性。
   - 第三个补丁在自测中加入了对 LSFE 的测试，确保其在用户空间的可用性。所有补丁均已提交并获得签名。

总体来看，本周的讨论集中在补丁的具体实现及其对用户空间和虚拟化环境的影响上，确保了新特性的可用性和兼容性。

#### 📝 邮件列表

1. **[08-18 20:21]** [PATCH v3 0/3] arm64: Support FEAT_LSFE (Large System Float
 Extension)
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[08-18 20:21]** [PATCH v3 1/3] arm64/hwcap: Add hwcap for FEAT_LSFE
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[08-18 20:21]** [PATCH v3 2/3] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[08-18 20:21]** [PATCH v3 3/3] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 17: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 22 Aug 2025 11:18:53 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题为“允许阴影阶段 2 读取故障”。该补丁的目的是处理在特定情况下可能出现的阶段 2 读取权限故障，尤其是在使用阴影映射时。

在历史讨论中，补丁的主要内容是允许在处理阴影阶段 2 故障时继续处理读取故障，而不是直接报错。Wei-Lin Chang 提到，虽然在正常情况下不应出现阶段 2 读取权限故障，但在某些情况下（如 L1 KVM 的不当配置）可能会触发此错误，因此需要对此进行处理。

本周的新讨论中，参与者对补丁进行了深入探讨。Oliver Upton 提到，KVM 创建没有读取权限的阶段 2 页表项的可能性较低，甚至可以考虑删除相关检查。Marc Zyngier 则表示，尽管 CPU 的 TLB 是短暂的，但 KVM 管理的 TLB 更为静态，放宽权限可能会导致问题。他建议在处理权限故障时应提前进行检查，并考虑在设计上进行更彻底的解决方案，而不是简单的修补。

总体而言，讨论集中在如何有效处理 KVM 中的权限故障以及补丁的必要性和设计方向上。

#### 📝 邮件列表

1. **[08-22 11:18]** [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[08-22 02:25]** Re: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[08-22 10:40]** Re: [PATCH] KVM: arm64: nv: Allow shadow stage 2 read fault
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 18: [PATCH v4 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR
 prior to initialization

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 21 Aug 2025 18:55:13 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vGIC（虚拟通用中断控制器）相关的补丁，具体是允许在初始化之前访问 GICD_IIDR 寄存器。

**原始补丁内容**：该补丁旨在修改对 GICD_IIDR 寄存器的访问权限，以便在 vGIC 初始化之前也能进行访问。

**之前的讨论要点**：在历史讨论中，参与者讨论了 ID 寄存器的访问逻辑，指出在 vGIC 初始化后，这些寄存器不能被修改，而其他寄存器则应在初始化后进行修改。Zhou Wang 提出了对当前逻辑的疑问，并希望确认自己的理解是否正确。

**本周的新讨论与进展**：本周的讨论中，Zhou Wang 和 Oliver Upton 进一步探讨了补丁的影响。Oliver 指出，如果允许在初始化前访问 GICD_IIDR，将会破坏现有的 ABI（应用二进制接口），因为该寄存器在初始化后已经是可写的。因此，唯一的解决方案是放宽对该寄存器的限制，允许在初始化前后都能访问。Zhou Wang 表达了对 Oliver 观点的理解和感谢，显示出讨论的积极进展。整体来看，参与者们在补丁的逻辑和影响上达成了一定的共识。

#### 📝 邮件列表

1. **[08-21 18:55]** Re: [PATCH v4 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR
 prior to initialization
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[08-21 11:43]** Re: [PATCH v4 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR
 prior to initialization
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[08-22 09:54]** Re: [PATCH v4 3/6] KVM: arm64: vgic-v3: Allow access to GICD_IIDR
 prior to initialization
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>

---

### Thread 19: [PATCH v10 0/6] KVM: arm64: Support FF-A 1.2

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Sat, 09 Aug 2025 02:33:18 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A 1.2 规范的补丁集（PATCH v10 0/6）。FF-A 1.2 引入了新的 SEND_DIRECT2 ABI，允许使用寄存器 x4-x17 作为消息载荷。该补丁集的主要目的是防止主机使用低于与虚拟机监控器（hypervisor）协商的 FF-A 版本，因为虚拟机监控器缺乏必要的兼容路径来进行版本转换。

在历史讨论中，Per Larsen 提到补丁集的具体内容，包括如何在初始化和主机处理程序中使用 SMCCC 1.2，以支持 FF-A 1.2 的功能。SMCCC 1.2 允许返回更多寄存器结果，简化了实现过程。

在本周的新讨论中，Will Deacon 对之前的补丁提出了一个小的拼写错误，并询问关于 FF-A 1.3 更新的可能内容，表示希望了解未来代码可能需要的调整方向。他还提到，去除 arm_smccc_1_1_smc() 宏中的零参数是一个积极的变化。

总体来看，当前的讨论集中在补丁的实现细节及未来可能的规范更新上。

#### 📝 邮件列表

1. **[08-09 02:33]** [PATCH v10 0/6] KVM: arm64: Support FF-A 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[08-09 02:33]** [PATCH v10 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[08-19 11:46]** Re: [PATCH v10 2/6] KVM: arm64: Use SMCCC 1.2 for FF-A
 initialization and in host handler
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 20: [PATCH v7 00/12] perf: arm_spe: Armv8.8 SPE features

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 14 Aug 2025 10:25:22 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARMv8.8 SPE 特性的补丁（PATCH v7 00/12），主要涉及支持三项新功能：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。这些特性相互独立，可以单独应用。补丁的具体内容包括对系统寄存器的更改以及对 Perf 工具的相应调整。

在历史讨论中，James Clark 提出了补丁的详细内容，并指出 FEAT_SPE_FDS 需要新增一个 `config4` 字段来支持数据源过滤，因为现有的 `perf_event_attr::configN` 字段已全部使用。该补丁得到了 Leo Yan 和 Ian Rogers 的审核和测试支持。

在本周的新讨论中，Ian Rogers 提出了一个与当前主题略有偏离的建议，认为应该推动另一个补丁的落地，以便通过 fdinfo 显示所有配置值，从而帮助工具更好地诊断 PMU 的繁忙状态。他提到该补丁虽然设计简洁，但目前仍处于停滞状态。

#### 📝 邮件列表

1. **[08-14 10:25]** [PATCH v7 00/12] perf: arm_spe: Armv8.8 SPE features
   - 发件人: James Clark <james.clark@linaro.org>
2. **[08-14 10:25]** [PATCH v7 08/12] perf: Add perf_event_attr::config4
   - 发件人: James Clark <james.clark@linaro.org>
3. **[08-18 08:51]** Re: [PATCH v7 08/12] perf: Add perf_event_attr::config4
   - 发件人: Ian Rogers <irogers@google.com>

---

### Thread 21: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge mappings

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 15 Aug 2025 17:26:55 +0100

#### 🤖 AI 总结

在本次邮件讨论中，主题为“[PATCH] KVM: arm64: 修复使用大页映射的非伙伴虚拟机的调试检查”。历史讨论中，Ben Horgan 提出了一个补丁，解决了在启用透明大页和 CONFIG_NVHE_EL2_DEBUG 时，调用 `assert_host_shared_guest()` 导致的调试检查失败问题。这一问题会在启动非伙伴虚拟机时触发 WARN_ON()，进而导致系统崩溃。补丁的核心在于更新调试检查逻辑，使其不再假设映射为单页，而是支持块映射。

在本周的新讨论中，Vincent Donnefort 对该补丁表示感谢，并确认了修复的有效性。他提到该补丁实际上是修复了之前提交的 f28f1d02f4ea 的问题，该提交引入了对映射大小的检查，尽管在当前版本中这一检查并未生效。Vincent 还对补丁进行了审核并给予了认可（Reviewed-by）。

综上所述，本周的讨论主要集中在对补丁的认可与确认上，未提出新的问题或争议。

#### 📝 邮件列表

1. **[08-15 17:26]** [PATCH] KVM: arm64: Fix debug checking for np-guests using huge mappings
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[08-18 14:03]** Re: [PATCH] KVM: arm64: Fix debug checking for np-guests using huge
 mappings
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 22: [PATCH] KVM: arm64: selftests: Sync ID_AA64MMFR3_EL1 in
 set_id_regs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 18 Aug 2025 17:41:00 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测试更新，具体是同步 ID_AA64MMFR3_EL1 寄存器的设置。

1. **原始 patch/问题的内容**：本次补丁旨在将 ID_AA64MMFR3_EL1 寄存器添加到 KVM 的自测试中，以确保在虚拟机环境中正确读取该寄存器的值。补丁的代码修改在 `set_id_regs.c` 文件中增加了一行代码，以同步该寄存器。

2. **之前的讨论要点**：在之前的讨论中，提到在增加对 ID_AA64MMFR3_EL1 的覆盖时，并未将其纳入到需要读取的寄存器列表中。这一遗漏需要通过本次补丁来修复。

3. **本周的新讨论、进展或结论**：本周的讨论主要集中在 Mark Brown 提交的补丁上，补丁已被确认并包含在代码中，修复了之前的遗漏。补丁的签署者为 Mark Brown，表明该修改已得到认可并准备合并到主干代码中。

总体而言，本次讨论有效地解决了 KVM arm64 自测试中的一个问题，确保了对 ID_AA64MMFR3_EL1 寄存器的正确处理。

#### 📝 邮件列表

1. **[08-18 17:41]** [PATCH] KVM: arm64: selftests: Sync ID_AA64MMFR3_EL1 in
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 23: [PATCH] KVM: arm64: Fix whitespace inconsistency in cpu_reg assignments

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 18 Aug 2025 06:39:42 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个格式修复补丁。补丁的主要内容是修正 `cpu_reg()` 赋值语句中等号周围的空格不一致问题，部分行使用了双空格而其他行则使用了单空格。为了提高代码的一致性，该补丁将所有赋值语句标准化为单空格。值得注意的是，这个补丁仅涉及格式调整，并不对功能产生影响。

在历史讨论中没有相关的背景信息或先前讨论内容，因此本周的新讨论是唯一的内容。参与者 lingfuyi 提交了这个补丁，并在邮件中详细说明了修复的目的和具体修改的文件。补丁已包含在 `arch/arm64/kvm/hyp/nvhe/hyp-main.c` 文件中，修改涉及到的行数为 8 行，进行了 4 次插入和 4 次删除。

总的来说，本周的讨论集中在这个格式修复补丁上，强调了代码风格一致性的重要性。

#### 📝 邮件列表

1. **[08-18 06:39]** [PATCH] KVM: arm64: Fix whitespace inconsistency in cpu_reg assignments
   - 发件人: lingfuyi@126.com

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH 00/16] KVM: arm64: Add "struct kvm_page_fault"

**📧 邮件数**: 19 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 21 Aug 2025 14:00:26 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中引入 `struct kvm_page_fault` 的 RFC（请求反馈补丁）。该补丁旨在优化处理页面故障的代码结构，并为未来的功能扩展（如 KVM Userfault）铺平道路。

### 1. 原始补丁内容
补丁的主要内容是添加一个新的结构体 `struct kvm_page_fault`，用于跟踪处理页面故障时的状态。此结构体将有助于减少传递给辅助函数的参数数量，并简化代码。

### 2. 之前讨论要点
在历史讨论中，参与者对补丁的初步想法表示支持，并讨论了如何在不影响功能的情况下重构代码。补丁的主要目标是提高代码的可读性和可维护性，同时为将来的功能扩展做好准备。

### 3. 本周的新讨论与进展
本周的讨论集中在补丁的具体实现细节上。Sean Christopherson 提出了多个补丁，逐步实现 `struct kvm_page_fault` 的各个方面，包括：
- 将与 VMA（虚拟内存区域）相关的信息整合到 `struct kvm_page_fault` 中。
- 提取 mmap_lock 保护的代码到新的辅助函数中，以提高代码的可读性。
- 讨论了如何更好地表示某些字段的命名，以提高代码的清晰度。

Oliver Upton 对补丁的可读性表示赞赏，并提出了一些命名上的改进建议，以便在架构中立代码中更好地使用该结构体。

总体来看，本周的讨论推动了补丁的进一步完善，参与者对补丁的方向表示积极支持，并提出了建设性的反馈。

#### 📝 邮件列表

1. **[08-21 14:00]** [RFC PATCH 00/16] KVM: arm64: Add "struct kvm_page_fault"
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[08-21 14:00]** [RFC PATCH 01/16] KVM: arm64: Drop nested "esr" to eliminate variable shadowing
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[08-21 14:00]** [RFC PATCH 02/16] KVM: arm64: Get iabt status on-demand
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[08-21 14:00]** [RFC PATCH 03/16] KVM: arm64: Move SRCU-protected region of
 kvm_handle_guest_abort() to helper
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[08-21 14:00]** [RFC PATCH 04/16] KVM: arm64: Use guard(srcu) in kvm_handle_guest_abort()
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[08-21 14:00]** [RFC PATCH 05/16] KVM: arm64: Introduce "struct kvm_page_fault" for
 tracking abort state
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[08-21 14:00]** [RFC PATCH 06/16] KVM: arm64: Pass kvm_page_fault pointer to transparent_hugepage_adjust()
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[08-21 14:00]** [RFC PATCH 07/16] KVM: arm64: Pass @fault to fault_supports_stage2_huge_mapping()
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[08-21 14:00]** [RFC PATCH 08/16] KVM: arm64: Add helper to get permission fault
 granule from ESR
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[08-21 14:00]** [RFC PATCH 09/16] KVM: arm64: Track perm fault granule in "struct kvm_page_fault"
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[08-21 14:00]** [RFC PATCH 10/16] KVM: arm64: Drop local vfio_allow_any_uc, use
 vm_flags snapshot
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[08-21 14:00]** [RFC PATCH 11/16] KVM: arm64: Drop local mte_allowed, use vm_flags snapshot
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[08-21 14:00]** [RFC PATCH 12/16] KVM: arm64: Move VMA-related information into
 "struct kvm_page_fault"
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[08-21 14:00]** [RFC PATCH 13/16] KVM: arm64: Stash "mmu_seq" in "struct kvm_page_fault"
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[08-21 14:00]** [RFC PATCH 14/16] KVM: arm64: Track "forced" information in "struct kvm_page_fault"
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[08-21 14:00]** [RFC PATCH 15/16] KVM: arm64: Extract mmap_lock-protected code to
 helper for user mem aborts
   - 发件人: Sean Christopherson <seanjc@google.com>
17. **[08-21 14:00]** [RFC PATCH 16/16] KVM: arm64: Don't bother nullifying "vma" in mem
 abort path
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[08-21 15:31]** Re: [RFC PATCH 05/16] KVM: arm64: Introduce "struct kvm_page_fault"
 for tracking abort state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
19. **[08-21 15:39]** Re: [RFC PATCH 00/16] KVM: arm64: Add "struct kvm_page_fault"
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

