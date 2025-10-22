# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 10:39:18

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

本邮件线程讨论了针对 Arm CCA（保密计算架构）在 KVM 中的支持，主要集中在一系列补丁（PATCH v10 00/43）上。这些补丁旨在实现对受保护虚拟机的支持，并解决了多个技术问题。

1. **原始补丁/问题内容**：补丁系列添加了在 KVM 中运行受保护虚拟机的支持，涉及到 Arm CCA 的实现。补丁的历史讨论中提到，相关的来宾支持已在 v6.14-rc1 中合并，因此不再需要单独处理。

2. **之前讨论要点**：之前的讨论主要集中在补丁的审查和修改建议上，包括修复潜在的崩溃问题、避免 RCU 停滞警告等。此外，补丁中还提到了一些对 VMM（虚拟机监控器）更新的要求，以及如何处理未委托失败的情况。

3. **本周的新讨论、进展或结论**：本周的讨论中，补丁逐一被提交并审查，涉及的内容包括：
   - 增加对 RMM（Realm 管理监视器）的支持，允许 VMM 设置 RIPAS（Realm IPA 状态）。
   - 处理 Realm 的 MMIO（内存映射输入输出）仿真。
   - 允许用户空间注入异常。
   - 提供对 SVE（可扩展向量扩展）的支持。
   - 增加对 Realm 的激活功能，确保在检测到 RMM 时启用相关功能。

总的来说，本周的讨论和补丁提交为 Arm CCA 在 KVM 中的实现奠定了基础，解决了多个技术细节，并确保了与现有系统的兼容性。

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

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 ARM64 架构上实现 SME（Scalable Matrix Extension）支持的补丁系列，主要内容如下：

1. **原始补丁/问题内容**：
   本次补丁系列（[PATCH v7 00/29]）旨在为 KVM 的 ARM64 实现 SME 支持，主要涉及对 SME 向量长度的配置、控制寄存器的访问、以及对 SME 特定状态的管理。

2. **之前讨论要点**：
   之前的讨论集中在如何将 SME 的实现与现有的 SVE（Scalable Vector Extension）功能集成，确保两者的向量长度配置不会相互干扰。补丁中提到的用户空间 ABI 设计，以及对寄存器访问的控制和异常处理也引起了关注。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论主要集中在补丁的具体实现细节上，包括对 SME 控制寄存器（如 SMCR 和 SVCR）的支持、对 ZA 和 ZT0 寄存器的访问、以及如何在上下文切换时管理 SME 状态。
   - 参与者 Mark Brown 提出了对用户空间访问 SME 特定寄存器的支持，并强调了在使用 SME 时需要注意的状态管理和异常处理。
   - 讨论中还涉及了对 KVM ABI 文档的更新，以反映 SME 的新特性和寄存器结构。
   - 另外，针对用户空间的测试用例也在讨论中被提及，以确保新功能的正确性和稳定性。

总体来看，本周的讨论进一步细化了 SME 支持的实现方案，并为后续的测试和文档更新奠定了基础。

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

本邮件线程讨论了针对 KVM 的 ARM SMMUv3 驱动的多个补丁（PATCH），主要集中在实现嵌套翻译和命令队列的仿真。

1. **原始补丁内容**：本次补丁系列（v4 版本）主要实现了 KVM 在 ARM 架构下对 SMMUv3 的支持，特别是通过“trap and emulate”方法实现嵌套 SMMUv3。补丁包括对命令队列（CMDQ）和流表（STE）的仿真，以及对 IOMMU 进行内存管理的功能。

2. **历史讨论要点**：之前的版本（v1-v3）尝试实现不同的功能，包括完整的 PV 接口和 DMA 隔离等，但由于维护复杂性，最终决定采用嵌套翻译的方式。历史讨论中提到的关键问题包括如何处理 SMMU 的 MMIO 空间仿真和如何确保驱动的可调试性。

3. **本周新讨论与进展**：本周的讨论主要集中在补丁的具体实现上，包括：
   - 增加了对 CMDQ 和 STE 的仿真，确保在主机和虚拟机之间的命令和状态正确传递。
   - 引入了对流表的仿真，确保在主机发出 CFGI_STE 命令时，能够正确更新超管的流表。
   - 讨论了如何处理 SMMU 的 GBPA 寄存器，确保其在主机禁用时返回 ABORT 状态。
   - 实现了对 io-pgtable 的支持，以便在 KVM 环境中进行内存分配。

整体来看，本周的补丁和讨论为 SMMUv3 驱动的实现打下了基础，确保了在 KVM 环境下的稳定性和性能。

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

本邮件线程讨论了对 pKVM（保护模式下的 KVM）支持的 Tracefs 功能的补丁系列，主要由 Vincent Donnefort 提出。以下是讨论的主要内容：

1. **原始补丁内容**：补丁系列的目标是为 pKVM 引入 Tracefs 支持，以便在保护模式下提供调试和性能分析工具。补丁包括创建远程事件和缓冲区的通用方法，并为 pKVM 超级管理程序添加支持。

2. **历史讨论要点**：之前的讨论集中在如何设计和实现 Tracefs 以支持 pKVM 的需求，包括环形缓冲区的实现、事件的定义和管理等。补丁经过多次迭代，逐步完善了功能和接口。

3. **本周新讨论与进展**：
   - 本周的邮件中，Vincent 提出了多个补丁，包括引入简单环形缓冲区、事件支持、Tracefs 接口的实现等。
   - 讨论了如何在 pKVM 超级管理程序中实现事件的创建与管理，使用 HYP_EVENT 宏简化事件的声明。
   - 还增加了对 Tracefs 的自测试支持，确保新功能的稳定性。
   - 讨论中提到的补丁包括对 Tracefs 目录的创建、事件的启用与禁用、以及对 Tracefs 接口的自测试等。

总体而言，本周的讨论和补丁推动了 pKVM 的 Tracefs 支持功能的实现，增强了对虚拟化环境的调试和监控能力。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 FEAT_RASv1p1 的支持及其选择。历史讨论中，Marc Zyngier 提出了一个包含六个补丁的系列，旨在填补 KVM 在 RAS（Reliability, Availability, and Serviceability）方面的不足。补丁的主要内容包括：添加 FEAT_RASv1p1 的能力标识、处理 RASv1p1 寄存器、忽略由 L1 客户机设置的 HCR_EL2.FIEN、使 ID_AA64PFR0_EL1.RAS 和 ID_AA64PFR1_EL1.RAS_frac 可写等。

在本周的新讨论中，参与者对补丁进行了审查并给予了认可。Cornelia Huck 和 Joey Gouly 对多个补丁进行了“已审核”反馈。Ben Horgan 提出了对 RASv1p1 寄存器处理的具体建议，并指出了代码中的一些潜在问题。最终，Marc Zyngier 确认了一些误解并表示将补丁应用于修复。

整体来看，本周的讨论主要集中在对补丁的审查和细节的讨论，推动了该系列补丁的进展。

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

本邮件线程讨论了针对 Linux 内核的一个补丁系列，主要是关于初始化 ARM 架构中的 SCTLR2_ELx 寄存器。该补丁系列共有五个部分，旨在为 ARMv8.8/ARMv9.3 及以后的版本提供对 SCTLR2_ELx 寄存器的支持，这些寄存器在未来的架构特性中将变得重要。

在历史讨论中，Yeoreum Yun 提出了补丁的背景，指出当前 Linux 内核并不严格需要修改 SCTLR2_ELx 寄存器，但为了避免在固件未正确初始化的情况下出现系统异常，建议在启动时初始化这些寄存器。此外，补丁还包括在 CPU 休眠和恢复时保存和恢复 SCTLR2_EL1 的值，以保持一致性。

在本周的新讨论中，Dave Martin 对各个补丁提出了具体的改进建议，包括代码风格、宏的使用和逻辑清晰度等。他强调了在补丁中清晰标注重大更改的重要性，并建议在代码中增加对潜在错误的检查，以提高可读性和安全性。Yeoreum Yun 对 Dave 的反馈表示感谢，并表示将根据建议进行修改。

总体而言，本周的讨论集中在补丁的细节优化和代码质量提升上，显示出开发者对提高内核稳定性和可维护性的关注。

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

本邮件线程讨论了针对 ARM64 架构的 TCR（Translation Control Register）相关宏的清理和更新工作，主要涉及四个补丁（PATCH 0/4 到 PATCH 4/4）。

1. **原始补丁内容**：补丁的主要目标是清理和更新 TCR_EL1、TCR_EL2 和 VTCR_EL2 的字段宏，确保它们在代码中的一致性和可读性。补丁中提到的更改包括添加新的寄存器字段定义，并用工具生成的 sysreg 格式替换旧的宏定义。

2. **之前讨论要点**：在历史讨论中，参与者对补丁的内容进行了初步审查，指出了宏定义不一致和可能导致的可读性问题。特别是对 EL1 和 EL2 的寄存器布局进行了讨论，强调了在 KVM 代码中保持清晰和一致的重要性。

3. **本周的新讨论与进展**：本周的讨论中，参与者针对补丁的具体实现细节提出了反馈，包括使用 `Enum` 而非 `UnsignedEnum` 的建议，以及对寄存器描述的准确性提出了质疑。Marc Zyngier 提到，使用 ARM ARM 文档中的寄存器信息可能会导致错误，建议使用 BSD 许可的 MRS 数据作为参考。此外，Anshuman Khandual 表示会根据反馈进行相应的修改。

总体而言，本周的讨论集中在补丁的细节和实现的准确性上，参与者们积极反馈并推动补丁的完善。

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

本邮件讨论的主题是关于为 KVM（Kernel-based Virtual Machine）在 arm64 架构上提供对受保护控制栈（GCS）的支持。GCS 是一种硬件特性，旨在增强对返回导向编程（ROP）攻击的防护，并简化应用程序的调用栈收集。

**原始 patch/问题内容**：
Mark Brown 提出的补丁系列（PATCH v15 0/6）旨在实现 KVM 客户机对 GCS 的支持。该补丁包括对 GCS 操作的管理、异常处理以及相关寄存器的配置。

**之前讨论要点**：
在历史讨论中，补丁经历了多次版本迭代，主要集中在如何管理 GCS 寄存器、异常处理以及与 KVM 的集成。讨论中提到，GCS 的实现需要确保硬件特性和指令的正确配置，以避免潜在的安全问题。

**本周的新讨论、进展或结论**：
本周的讨论中，Mark Brown 提出了六个具体补丁，涵盖了 GCS 寄存器的管理、异常转发、PSTATE.EXLOCK 的设置等。参与者 Marc Zyngier 对某些补丁提出了具体的改进建议，强调了对 GCS 异常的处理和寄存器访问的必要性。整体来看，补丁系列正在逐步完善，目标是确保 GCS 功能在 KVM 客户机中的有效实现。

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

本邮件线程讨论的主题是关于 KVM（内核虚拟机）对中介虚拟性能监控单元（mediated vPMUs）的支持，具体内容包括一系列补丁（patch）和相关讨论。

1. **原始补丁内容**：Sean Christopherson 提出了一个补丁系列，旨在为 KVM 添加对中介 vPMUs 的支持。补丁包括对性能监控单元（PMU）相关的清理和改进，特别是针对 x86 架构的实现。

2. **之前讨论要点**：在历史讨论中，参与者们探讨了如何在不影响系统稳定性的情况下处理中介 PMU 的中断和状态切换。Peter Zijlstra 提出了一些关于 LVTPC（本地向量定时器控制寄存器）切换的安全性和实现细节的疑问，特别是涉及到中断处理和性能监控的上下文切换。

3. **本周的新讨论和进展**：本周的讨论集中在如何安全地处理在 PMI（性能监控中断）期间的 VM-exit（虚拟机退出）。参与者们讨论了在处理 PMI 时可能遇到的状态不一致问题，并确认了在不同架构下的 PEBS（精确事件采样）记录处理方式。Xudong Hao 报告了在多个 Intel 平台上测试的结果，表明中介 vPMU 和传统的基于性能的 vPMU 均未发现问题，测试通过率良好。此外，Anup Patel 对 RISC-V 的相关补丁表示认可。

总体而言，讨论围绕着如何在 KVM 中实现中介 vPMUs 的支持，确保系统的稳定性和性能，同时也展示了测试的积极结果。

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

本邮件线程讨论了一个关于支持 Armv9.6 的 FEAT_LSUI 特性的补丁集，该特性允许内核在不清除 PSTATE.PAN 位的情况下访问用户内存，主要应用于 futex 原子操作。

**原始补丁内容**：
补丁集包含五个部分，主要目的是在 futex 原子操作中应用 FEAT_LSUI，替代传统的 ldxr/stlxr 指令对，简化内存访问并提高性能。

**之前讨论要点**：
在历史讨论中，参与者讨论了使用 uaccess_disable_privileged() 函数的必要性，强调用户和内核可能对标签检查的设置不同，使用 FEAT_LSUI 时需谨慎处理这些差异。Catalin Marinas 提出了对 MTE 标签检查的关注，并指出在使用 FEAT_LSUI 时可能需要启用 TCO（标签检查覆盖）。

**本周新讨论进展**：
本周的讨论进一步探讨了在使用 LSUI 指令时是否需要启用 TCO。Catalin Marinas 强调，若不启用 TCO，可能会导致内核在访问用户内存时出现不一致的标签检查行为。Yeoreum Yun 最终确认，当前的实现并未启用 TCO，且在使用 LSUI 指令时可能需要重新考虑这一点，以避免潜在的错误报告。

总体来看，本周的讨论集中在确保内核访问用户内存时的一致性和安全性上，特别是在标签检查的上下文中。

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

本邮件线程讨论了对 Armv8.7 架构中 FEAT_{LS64, LS64_V} 特性的支持，涉及一系列补丁（patch）以实现该功能。

1. **原始 patch/问题内容**：
   Yicong Yang 提出了一个补丁系列（PATCH v5 0/7），旨在添加对 Armv8.7 中 FEAT_{LS64, LS64_V} 的支持。这些特性允许进行单拷贝原子 64 字节的加载和存储操作，并通过 HWCAP3 和 cpuinfo 向用户空间暴露这些特性。

2. **之前讨论要点**：
   在之前的讨论中，补丁的设计考虑了如何在虚拟机中处理不支持的内存访问，以及如何在用户空间中实现这些新指令的支持。Marc Zyngier 的补丁处理了在虚拟机中对 LS64 指令的异常处理。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Yicong Yang 提交了多个补丁，主要包括：
   - 向 KVM 添加对 FEAT_{LS64, LS64_V} 的支持，并在虚拟机中启用相关特性。
   - 增加了对这些特性的文档说明，确保用户空间能够理解如何处理相关的异常。
   - 添加了 HWCAP 测试，以验证这些特性在不同内存类型下的行为。
   - 进行了多次补丁更新，修复了冲突，并对补丁进行了重组，以确保 KVM 处理优先于特性支持。

整体而言，这些补丁的实施将增强 Arm64 架构在虚拟化环境中的性能和功能，特别是在处理复杂的内存操作时。

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

本邮件讨论的主题是关于为 KVM（Kernel-based Virtual Machine）在 arm64 架构中支持 FF-A（Firmware Framework for Arm）1.2 版本的补丁集。补丁集包含六个部分，主要目的是引入新的 SEND_DIRECT2 ABI，并确保主机不会使用低于已与虚拟机监控器协商的 FF-A 版本。

在历史讨论中，补丁的背景涉及到 FF-A 1.2 规范的引入，特别是新的消息接口 FFA_MSG_SEND_DIRECT_REQ2 的支持。补丁集更新了所有 SMC（Secure Monitor Call）调用，以使用 SMCCC 1.2，从而简化了需要接受超过 8 个参数或返回超过 4 个值的接口的支持。

本周的新讨论中，Per Larsen 提出了补丁的具体实现和修改，包括：
1. **补丁 1**：修正主机版本降级尝试时的返回值，确保协商的 FF-A 版本保持锁定。
2. **补丁 2**：在 FF-A 初始化和主机处理程序中使用 SMCCC 1.2，以支持更多的返回寄存器。
3. **补丁 3 和 4**：将 FFA_NOTIFICATION_* 调用和 FF-A 1.2 的可选接口标记为不支持，以防止它们被错误地代理。
4. **补丁 5**：在读取 FFA_FEATURE 调用的最小缓冲区大小时，掩码掉其他位。
5. **补丁 6**：将支持的 FF-A 版本提升至 1.2，以启用 1.2 特有的消息接口。

所有补丁均获得了 Will Deacon 的认可，显示出社区对该补丁集的支持和认可。整体来看，本周的讨论集中在确保 FF-A 1.2 的兼容性和功能实现上。

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

本邮件讨论的主题是关于在 Linux 中初始化 SCTRL2_ELx 寄存器的补丁系列（[PATCH v4 0/5]）。该系列补丁旨在为 ARM 架构的 Linux 内核提供对 SCTLR2_ELx 寄存器的初步支持，这一特性从 ARMv8.8/ARMv9.3 开始为可选，ARMv8.9/ARMv9.4 起为强制要求。

在历史讨论中，补丁经历了多个版本的迭代，主要改进包括合并函数、修复寄存器设置错误以及在 CPU 启动时初始化 SCTLR2_ELx 寄存器等。

本周的新讨论中，Yeoreum Yun 提出了五个补丁：
1. **补丁 1**：使 SCTLR2_EL1 在 EL1 运行时可访问。
2. **补丁 2**：在 CPU 启动时初始化 SCTLR2_ELx 寄存器，以防止因未初始化而导致的系统异常。
3. **补丁 3**：在 CPU 休眠和恢复过程中保存和恢复 SCTLR2_EL1 的值，确保一致性。
4. **补丁 4**：在通过 kexec 启动新内核之前显式初始化 SCTLR2_ELx 寄存器，避免其保留任意值。
5. **补丁 5**：支持在每个任务基础上配置 SCTLR2_EL1，以便未来使用相关功能。

这些补丁的讨论和修改旨在增强 ARM 架构的 Linux 内核对新特性的支持，并确保系统的稳定性和一致性。

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

本邮件讨论的主题是针对 KVM（内核虚拟机）在 arm64 架构下的一个内核 BUG 的修复。原始的补丁（patch）旨在解决由于不当回溯（bad backport）导致的内核错误，具体是与 FPSIMD/SVE/SME 状态的保存和刷新相关。该补丁的背景是，之前的上游提交依赖于在 `fpsimd_save_and_flush_cpu_state()` 函数中禁用中断，以防止在保存主机浮点上下文时触发软中断，但在某些稳定内核版本中，这一条件未得到满足，导致了实际使用中的 BUG。

在历史讨论中，补丁的作者 Will Deacon 指出，由于某些稳定内核未能正确处理中断，导致 `kernel_neon_begin()` 中的 BUG_ON(!may_use_simd()) 被触发，进而引发内核崩溃。为了解决这个问题，Deacon 提出了一个简单的修复方案，使用软中断安全的 `get_cpu_fpsimd_context()` 和 `put_cpu_fpsimd_context()` 函数替代原有的实现。

在本周的新讨论中，Greg Kroah-Hartman 确认已经将该补丁添加到多个稳定内核版本（包括 5.15、6.1 和 6.6）中，并提供了补丁的下载链接。这表明该补丁已获得认可并被正式应用于稳定版本中。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在处理 ARM64 架构的阶段-2 页表销毁时的调度问题。原始的补丁（PATCH v2 0/2）旨在解决在突然销毁一个完全映射的 128G 虚拟机时，出现的调度警告，尤其是在非强制抢占的内核配置下（CONFIG_PREEMPT_NONE=y）。

历史讨论中，补丁的主要内容包括将 `kvm_pgtable_stage2_destroy()` 函数拆分为两个部分：一个用于执行页表遍历并释放地址范围内的条目，另一个用于释放 PGD（Page Global Directory）。这样可以在处理大页表时，定期调用 `cond_resched()` 以避免长时间占用 CPU。

在本周的新讨论中，Raghavendra Rao Ananta 提出了两个补丁的具体实现，并进行了详细说明。补丁 1 拆分了销毁函数，补丁 2 则在销毁过程中定期检查调度条件以避免 CPU 占用过高。Oliver Upton 对补丁表示认可，并确认已将其应用于修复中。

总结来说，本周的进展是补丁已被采纳，解决了在销毁大虚拟机时的调度警告问题，提升了 KVM 的稳定性和性能。

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

本邮件讨论的主题是对 ARM64 架构中支持 FEAT_LSFE（大系统浮点扩展）的补丁。FEAT_LSFE 是从 v9.5 开始可选的功能，旨在为浮点值的原子内存操作提供新指令。尽管当前内核没有对该功能的直接需求，但补丁提供了一个硬件能力（hwcap），以便用户空间能够识别该功能，并允许 KVM 客户机访问相关的 ID 寄存器字段。

在历史讨论中，补丁经历了多个版本的更新，主要修复了 hwcap 测试中的问题，并进行了代码重组。补丁的主要内容包括：
1. 为 FEAT_LSFE 添加 hwcap。
2. 在 KVM 中向客户机暴露 FEAT_LSFE。
3. 在自测试中增加对 LSFE 的测试。

本周的新讨论中，Mark Brown 提出了三个补丁的具体实现，包括：
1. 在 `hwcap` 中添加 FEAT_LSFE 的支持。
2. 在 KVM 中暴露 FEAT_LSFE 相关的 ID 寄存器字段。
3. 在自测试中增加 LSFE 的测试用例，确保其在用户空间的可用性。

整体来看，本周的讨论集中在补丁的具体实现和测试上，标志着对 FEAT_LSFE 支持的进一步推进。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理影子二级页表（shadow stage 2）读取权限故障的补丁。补丁的目的是允许在处理影子二级页表时继续处理读取故障，而不是直接报错，因为在某些情况下，L1 可能会为 L2 创建没有读取权限的映射。

在之前的讨论中，Wei-Lin Chang 提到，尽管在正常情况下不应出现二级读取权限故障，但在某些特殊情况下（如 L1 的不当配置），可能会触发此错误。他提出需要考虑如何处理这些边缘情况，同时指出 TLB（Translation Lookaside Buffer）是短暂的，因此在某些方面是可以接受的。

本周的新讨论中，Oliver Upton 和 Marc Zyngier 对补丁进行了深入分析。Oliver 提到，KVM 创建没有读取权限的二级页表项的可能性较低，建议可以考虑删除相关检查。Marc 则强调了 KVM 管理的 TLB 的静态特性，并提出在实际硬件上可能会出现的问题，建议在处理权限故障时应更为谨慎，并考虑跟踪写权限位的复杂性。他们一致认为当前的补丁是合理的，但也对未来的设计提出了更高的要求。

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

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主题是允许在初始化之前访问 GICD_IIDR 寄存器。该补丁的目的是为了改善虚拟化环境中对 GIC（通用中断控制器）寄存器的访问控制。

在之前的讨论中，参与者对寄存器的访问逻辑进行了分析，指出 ID 寄存器在 vGIC 初始化后不可修改，而其他寄存器则应在初始化后进行修改。Zhou Wang 提出了对补丁逻辑的疑问，认为代码应当在特定条件下返回错误。

本周的新讨论中，Oliver Upton 进一步解释了补丁的意图，强调 GICD_IIDR 寄存器在初始化后是可写的，因此需要放宽对该寄存器的访问限制，使其在初始化前后均可访问。他还提到，ID 寄存器的理想语义是初始化前可读写，初始化后只读。Zhou Wang 对此表示理解并感谢 Oliver 的帮助。

总体来看，本周的讨论集中在对补丁逻辑的澄清和寄存器访问语义的确认上，推动了补丁的进一步完善。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构上支持 FF-A 1.2 规范的补丁集（PATCH v10 0/6）。FF-A 1.2 规范引入了新的 SEND_DIRECT2 ABI，允许使用 x4-x17 寄存器作为消息有效载荷。该补丁集的目的是防止主机使用低于与虚拟机监控器（hypervisor）协商的 FF-A 版本，因为虚拟机监控器缺乏必要的兼容性路径来转换 FF-A 版本。

在之前的讨论中，Per Larsen 提到使用 SMCCC 1.2 进行 FF-A 初始化的重要性，SMCCC 1.2 增加了可以返回的寄存器数量，这对于实现 FF-A 特性是必要的。

本周的新讨论中，Will Deacon 对之前的补丁提出了一些问题，询问关于 FF-A 1.3 更新的可能内容，以便为未来的代码调整做好准备。同时，他也提到，消除 arm_smccc_1_1_smc() 宏中多余的零参数是一个积极的改进。这表明参与者对补丁的实现效果表示认可，同时对未来的规范更新保持关注。

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

本邮件线程讨论了与 Armv8.8 SPE 特性相关的补丁（PATCH v7 00/12），主要涉及三个新特性：FEAT_SPEv1p4 过滤器、FEAT_SPE_EFT 扩展过滤和 SPE_FEAT_FDS 数据源过滤。这些特性可以独立应用，补丁分为多个部分，包括对系统寄存器的更改和性能工具的相应调整。

在历史讨论中，James Clark 提出了补丁的背景，强调了新增的 `config4` 字段的必要性，以支持 SPE_FEAT_FDS 特性，因为现有的 `perf_event_attr::configN` 字段已被占用。该补丁得到了 Leo Yan 和 Ian Rogers 的审核和测试支持。

在本周的新讨论中，Ian Rogers 提出了一个与当前补丁略有偏离的建议，认为应该推动另一个补丁的合并，以便通过 fdinfo 显示所有配置值，从而帮助工具更好地诊断 PMU 的繁忙状态。尽管该补丁尝试保持简洁，但目前仍处于停滞状态。整体来看，讨论集中在如何增强性能监控和工具的可用性上。

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

本邮件讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下修复针对使用大页映射的非持久性虚拟机（np-guest）的调试检查问题。

**原始 patch 内容**：
Ben Horgan 提出的补丁旨在解决在启用透明大页和 CONFIG_NVHE_EL2_DEBUG 时，`assert_host_shared_guest()` 函数中的调试检查失败的问题。这一问题会导致系统崩溃。补丁建议更新检查逻辑，使其不再假设映射为单个页面，而是接受块映射的情况。

**之前讨论要点**：
在历史讨论中，Horgan 详细描述了问题的根源，并指出需要在 `__pkvm_host_relax_perms_guest()` 和 `__pkvm_host_mkyoung_guest()` 函数中进行相应的修复，以确保调试检查的准确性。

**本周的新讨论**：
在本周的讨论中，Vincent Donnefort 对该补丁表示感谢，并确认了修复的有效性。他提到此修复与之前的提交（f28f1d02f4ea）相关，后者引入了对映射大小的检查。Donnefort 还在邮件中表示已对补丁进行了审核（Reviewed-by）。

总体来看，该讨论集中在修复 KVM 在特定条件下的调试检查问题上，确保系统稳定性和可靠性。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测试（selftests）中，如何同步 ID_AA64MMFR3_EL1 寄存器的内容。

**原始 patch/问题的内容**：
本次 patch 的目的是在 KVM 的自测试代码中，将 ID_AA64MMFR3_EL1 寄存器添加到读取的寄存器列表中。之前在添加对该寄存器的覆盖时，未将其包含在访客（guest）环境中读取的寄存器列表中。

**之前讨论要点**：
由于本邮件没有提供历史讨论的内容，因此没有相关的讨论要点可供总结。

**本周的新讨论、进展或结论**：
本周的讨论主要集中在 Mark Brown 提交的 patch 上，具体修改了 `set_id_regs.c` 文件，增加了对 ID_AA64MMFR3_EL1 寄存器的同步。此修改修复了之前未能同步该寄存器的问题，确保了 KVM 在 arm64 架构下的自测试能够正确反映该寄存器的状态。该 patch 的提交被标记为修复了之前的提交（0b593ef12afc），并由 Mark Brown 签署。

#### 📝 邮件列表

1. **[08-18 17:41]** [PATCH] KVM: arm64: selftests: Sync ID_AA64MMFR3_EL1 in
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 23: [PATCH] KVM: arm64: Fix whitespace inconsistency in cpu_reg assignments

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 18 Aug 2025 06:39:42 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个格式修复补丁。补丁的主要内容是修复 `cpu_reg()` 赋值时等号周围的空格不一致问题，标准化为单个空格，以提高代码的一致性。该补丁并不涉及功能上的变化，仅为格式调整。

在历史讨论中没有相关内容，因此本周的新讨论是唯一的邮件。参与者 lingfuyi 提出了这个补丁，并详细描述了修复的具体内容，包括在 `arch/arm64/kvm/hyp/nvhe/hyp-main.c` 文件中进行了 4 次插入和 4 次删除，以统一空格格式。

总结而言，本周的讨论集中在对代码格式的规范化上，确保代码风格的一致性，提升了代码的可读性。

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

本邮件线程讨论了一个关于 KVM (Kernel-based Virtual Machine) 的补丁系列，主要集中在为 arm64 架构引入一个新的结构体 `struct kvm_page_fault`，以改进处理页面故障的方式。

1. **原始补丁/问题内容**：
   - 补丁的核心是添加 `struct kvm_page_fault`，旨在简化故障处理路径，并为未来的功能（如 KVM Userfault）铺平道路。该补丁的实现主要是代码重组，没有引入新的功能。

2. **之前讨论要点**：
   - 之前的讨论主要围绕如何通过新的结构体来优化故障处理的代码，减少参数传递的复杂性，并提高代码的可读性。参与者对补丁的总体方向表示支持，但也提出了一些具体的改进建议，例如对字段名称的调整，以便更好地与现有术语对齐。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论中，Sean Christopherson 提出了多个补丁，逐步实现 `struct kvm_page_fault` 的功能，包括跟踪故障状态、简化代码逻辑、提取 mmap 锁保护的代码等。Oliver Upton 对补丁的可读性表示赞赏，并建议对某些字段进行重命名以提高清晰度。整体来看，补丁系列在代码结构和可读性方面取得了积极进展，参与者对未来的改进持乐观态度。

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

